# Time-limited production AWS access for selected agents

Status: Parked idea, recorded 2026-10-08. Nothing has been built. Come back to it before writing any code.

## The idea

Sandbox AWS stays as it is today: a blanket grant. When the AWS Gate is open on the phone, every agent on the host can use the sandbox account.

Production should be different. From the phone, I pick one aplexer session (that is, one agent), choose a role and a short TTL, confirm with biometrics, and only that session gets production credentials until the grant expires or I revoke it.

The phone side would be a PocketShell extension rather than the separate AWS Gate app.

## What exists today (as of 2026-10-08)

- AWS Gate is `phone-aws-auth` (repo `alexeygrigorev/phone-aws-auth`, copy in `aws-infra/sandbox/phone-aws-auth`).
  - The phone writes `{active, expires_at}` to a per-host DynamoDB row, `phone-aws-gate`.
  - The host's `credential_process` calls a vendor Lambda with a per-host bearer. The Lambda checks the row and returns 15-minute STS credentials for `phone-aws-sandbox-role`, which has `Action:*`.
  - The grant scope is the whole host. The phone holds a long-lived controller IAM key.
- aplexer has no auth model beyond the Unix user.
  - Each session has a stable UUID and a 0600 control socket.
  - Every operation on a session goes through `src/worker/connection.rs::dispatch_operation`.
  - A session runs exactly one agent, so "this agent" means "this session UUID". Nested sessions carry `parent_session`.
- PocketShell has no plugin or extension system.
  - The UI hides missing platform features via `pocketshell-core/packages/ui/src/app/platformCapabilities.ts`.
  - Login is Google OAuth through `pocketshell-sync`. It is required on web and optional on Android and desktop.
  - Android lists aplexer sessions over SSH via `pocketshell sessions`. Desktop and web call `a snapshot --json`.
- `aws-infra/main/cmp/iam_alert_investigator.tf` lets `phone-aws-sandbox-role` assume the read-only `cmp-alert-investigator` role in the main (production) account. Any agent with the sandbox gate open can therefore already read CMP production logs and diagnostics without a per-agent grant.

## Proposed design

### Grant flow

1. In PocketShell, open a session's menu and choose "Grant prod AWS". Pick a role and a TTL, then confirm with biometrics. The app sends the grant to `pocketshell-sync`, authenticated by Google login plus a signature from a hardware-backed device key, so a stolen Google token cannot create grants.
2. The grant is stored as a row keyed by (host, aplexer session UUID, role) with `expires_at` and the approver.
3. Inside the session, AWS tools use a `prod` profile whose `credential_process` is a new `a aws-credentials` command.
   - The command asks the session's own aplexer worker to vouch for the caller. The worker checks via `SO_PEERCRED` that the caller is a descendant of the session's process.
   - The worker then requests credentials for its own session UUID.
   - The profile can be configured host-wide, because sessions without a grant are simply refused.
4. A broker Lambda verifies the grant and assumes the production role. It tags the role session with the aplexer session UUID, so CloudTrail shows which agent acted, and returns 15-minute credentials.
5. aplexer sends a message to the agent, for example "prod access until 14:30, use AWS_PROFILE=prod".
6. To revoke, delete the row, and add an instant kill: a deny on `aws:TokenIssueTime` before the revocation time. Revocation works from every platform.

### Roles in the main account (new Terraform root `aws-infra/main/agent-access/`)

- `agent-prod-readonly`: logs, alarms, describe and list across production apps. This is a generalization of `cmp-alert-investigator`.
- Scoped job roles, such as restarting a service, running a one-off task or reading snapshots. Add one only when a concrete need appears.
- `agent-prod-admin`: break-glass access for when I am away from my laptop.
  - Maximum 30 minutes, and only one session can hold it at a time.
  - Requires a distinct confirmation screen in the app and sends a notification on every grant.
  - Explicitly denies the actions an agent could use to keep access after the grant ends: creating IAM users or access keys, modifying the agent-access roles and the grant system, and stopping CloudTrail. Everything else is allowed.
- All roles trust only the broker Lambda's execution role, require the session tag, and have a 1-hour maximum session duration.
- Deploys stay with GitHub OIDC (`main/common/github_oidc.tf`).

Decided: switch `cmp-alert-investigator`'s trust from `phone-aws-sandbox-role` to the broker, so nothing in production is reachable without a grant.

### PocketShell extensions

- Extensions are built in, not a runtime plugin loader. Play's downloaded-code policy, web CSP, and the trust needed for prod-granting code all rule a loader out.
- An extension registry in `packages/ui` declares, per extension: name, supported platforms, whether login is required, and UI entry points (session-row action, settings page, status badge).
- Installing means toggling the extension in Settings > Extensions. Enabled extensions are stored per account in `pocketshell-sync` and returned by `/me`, so they follow the account to every device.
- The host side is installed with `pocketshell extension install aws-gate`, which writes the `prod` AWS profile and checks the aplexer version.
- This feature requires login.
- Platform support:
  - Android: full support and the first target, because of biometrics.
  - Desktop: OS authentication, or revoke-only at first.
  - Web: view and revoke only, until passkey approval exists.

## Known limit

All sessions run as the same Unix user. The worker's ancestry check stops accidental or casual use from another session, but a hostile process could still read another session's credentials from `/proc` or its environment. The real boundary would be running prod-granted sessions as a separate Unix user or in a sandbox. That is a later phase, not v1.

## Phases

1. aws-infra:
   - broker and grants table in `sandbox/phone-aws-auth`
   - `main/agent-access/` roles
   - move the CMP investigator's trust to the broker
   - instant revoke

   Plan only; I apply production IAM changes myself.
2. aplexer: a worker operation that verifies the caller belongs to the session, the `a aws-credentials` command, and the grant notification message.
3. pocketshell-sync: create, list and revoke grant endpoints with device-key signatures.
4. PocketShell: the extension registry and the AWS grants extension on Android, with a countdown badge on granted sessions.
5. Desktop and web support, and separate-uid isolation for prod-granted sessions.

## Open questions

- Default and maximum TTL per role. The starting suggestion is 15 minutes default and 1 hour maximum, with admin capped at 30 minutes.
- Should child sessions (`parent_session`) inherit a grant? The default suggestion is no.
- Does the standalone AWS Gate app stay for sandbox, or does sandbox also move into the extension?
- Exact permissions of `agent-prod-readonly` beyond what CMP needs.
