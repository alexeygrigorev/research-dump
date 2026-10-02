# Browser access from headless Codex with YOLO

**Tested:** October 2, 2026, on Windows using PowerShell, Codex CLI 0.160.0, and model `gpt-6.1-sol`.

## Result

Codex running non-interactively successfully used the connected Chrome browser integration. It opened Google, entered the exact query `can codex use the browser when its running in headless mode?`, submitted the search, and opened and read the first organic result.

This demonstrates browser access from a headless Codex process in the tested environment. It does not establish that Chrome itself ran headlessly or that a standalone CLI installation automatically has the same browser integration.

## Command used

Run this in PowerShell with an authenticated Codex CLI and the browser integration already available:

```powershell
codex.cmd exec --dangerously-bypass-approvals-and-sandbox --skip-git-repo-check --color never "Use the available browser integration to open Google, type the exact query 'can codex use the browser when its running in headless mode?', submit the search, then open and check the first organic search result. This is a test of browser access from headless Codex. Use actual browser interaction, and report whether it worked, the first result title and URL, and a brief summary. If browser access fails, report the exact blocker honestly. Do not install or modify configuration."
```

- `exec` runs Codex non-interactively, without its interactive terminal UI.
- `--dangerously-bypass-approvals-and-sandbox` enables the requested YOLO behavior: no approval prompts and no sandbox. The startup output confirmed `approval: never` and `sandbox: danger-full-access`.
- `--skip-git-repo-check` permits this task outside a Git repository; the test ran from `C:\Users\alexey`.
- `--color never` keeps captured output plain.
- `codex.cmd` uses the Windows command shim. Calling `codex` initially selected `codex.ps1`, which PowerShell blocked because script execution was disabled. Using the `.cmd` shim worked without changing execution policy.

On other platforms, use the installed `codex` executable in place of `codex.cmd`.

## Browser path and observed behavior

1. The child Codex process read the installed Browser skill at `C:/Users/alexey/.codex/plugins/cache/openai-bundled/browser/26.928.21956/skills/control-in-app-browser/SKILL.md`.
2. It invoked the `node_repl/js` tool to use the browser integration. The completed run reported that it connected through Chrome.
3. It performed the Google search through actual browser interaction.
4. The first organic result was [Headless browser to help codex verify](https://www.reddit.com/r/codex/comments/1s64upa/headless_browser_to_help_codex_verify/).
5. Clicking that result left the Google page unchanged. Navigating directly to the result's URL succeeded, and Codex read the thread.
6. Codex reported that the thread discussed browser verification with Playwright, remote-debugging Chrome, and Chromium reading page elements without a visible window. This is a summary of the child process's report, not independent validation of those suggestions.
7. The process finished successfully with exit code 0. No installation or configuration changes were made.

The run also saved a local screenshot to `C:/Users/alexey/browser-access-test.png`; the screenshot is not included in this repository.

## Reusing the approach

Keep `codex exec` and replace the prompt with the desired browser task. Specify the site, exact input, expected navigation, and what evidence to report. Ask for actual browser interaction and an honest blocker report so a web-search answer is not mistaken for a successful browser test.

The browser tooling must be available to the child process. In this test, the installed Browser skill and `node_repl/js` tool were accessible; no browser setup was performed. YOLO changes approvals and sandboxing, but does not by itself provide browser tools. If a result click does not navigate, opening the observed result URL directly is a useful fallback.

## Reference

[Official OpenAI documentation: non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode). The command flags above were also checked against the locally installed `codex.cmd exec --help` output.
