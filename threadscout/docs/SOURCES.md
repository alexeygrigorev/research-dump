# Проверенные первичные источники

Проверка: **18 сентября 2026**. URL сохранены для воспроизводимости. В пакет не включены полные копии чужих публикаций, персональные сообщения или закрытые материалы. Цены, разрешения, правила и интерфейсы необходимо перепроверять при изменении поведения.

| ID | Источник | Что подтверждает / границы |
|---|---|---|
| S01 | https://alexeygrigorev.com/ | Публичный профиль, курсы, проекты и ссылка на блог |
| S02 | https://datatalks.club/people/alexeygrigorev.html | DataTalks.Club, проектные ML/DE/MLOps/LLM-направления |
| S03 | https://alexeygrigorev.com/projects.html | minsearch, AI Engineering Field Guide и другие проекты; статистика stars не переносилась |
| S04 | https://aishippinglabs.com/ | Практические AI-проекты и сообщество; коммерческие memberships не обозначаются бесплатными |
| S05 | https://aishippinglabs.com/blog/telegram-writing-assistant | Собственный локальный Telegram/Claude Code/Markdown workflow; статья 30.01.2026 |
| S06 | https://aishippinglabs.com/blog/sqlitesearch | Собственная лёгкая Python search-библиотека; статья 20.02.2026; performance claims не подтверждались независимыми тестами |
| S07 | https://news.ycombinator.com/newsguidelines.html | Запрет AI-generated и AI-edited публичного текста, ограничения продвижения |
| S08 | https://github.com/HackerNews/API | Официальный read API; документированного write endpoint нет |
| S09 | https://hn.algolia.com/api | Поиск HN; индекс не тождественен официальному актуальному item API |
| S10 | https://developers.openai.com/codex/noninteractive/ | codex exec, stdin, JSON schema, read-only, ephemeral, ignore-user-config, сохранённая авторизация; редирект на ChatGPT Learn |
| S11 | https://developers.openai.com/codex/auth/ | ChatGPT sign-in отдельно от API-key billing |
| S12 | https://developers.openai.com/codex/config-reference/ | forced_login_method, web_search и feature settings; реальная установленная версия ещё требует проверки |
| S13 | https://core.telegram.org/bots/api | Long polling, inline buttons, CopyTextButton 1–256 символов |
| S14 | https://core.telegram.org/bots/webapps#validating-data-received-via-the-mini-app | Подписанный initData, HMAC и проверка auth_date; мобильная clipboard-совместимость не проверена |
| S15 | https://support.reddithelp.com/hc/en-us/articles/24368958859668-Sign-up-for-Reddit-Pro | Регистрация, verified email, SFW, business/organization setup |
| S16 | https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy | API approval, письменное согласование коммерческого сценария, ограничения автоматизации; обновлено 05.06.2026 |
| S17 | https://www.business.reddit.com/pro | Бесплатный Reddit Pro; старт https://www.reddit.com/reddit-pro |
| S18 | https://support.reddithelp.com/hc/en-us/articles/47619216411284-Reddit-Pro-Feature-Trends | Ключевые слова, неполный English/SFW охват, запрет выгрузки чужих данных вручную и автоматически |
| S19 | https://aishippinglabs.com/blog/ai-engineering-hiring-manager-interview | Заголовок/описание и free with sign-in; полный текст не прочитан |
| S20 | https://support.reddithelp.com/hc/en-us/articles/47619289307412-Reddit-Pro-Feature-Links | Publisher Links, domain verification, свои RSS/URL, desktop; RSS не автопостинг |
| S21 | https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/ | Бесплатный временный Quick Tunnel для разработки, не production SLA |

## Что не удалось подтвердить в этой среде

Работу сети из Python (DNS недоступен), живую доставку Telegram, локальную версию/авторизацию Codex пользователя, аккаунт/разрешение Reddit, запуск Mini App на телефоне, доступность и parsing RSS `aishippingblog.com/feed`. Правила предложенных сабреддитов не проверены. Числа о конверсии или обещания маркетингового результата не использованы.
