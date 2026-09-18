# Отчёт о проверке

Дата: 18 сентября 2026. Среда: Linux, Python 3.13.5. Заявленный минимум 3.11; отдельный прогон на 3.11/macOS/Windows не выполнен.

## Выполнено

```text
python -m unittest discover -s tests -v
Ran 54 tests
OK

python -m compileall -q threadscout
exit 0

python -m threadscout doctor
exit 0; no credentials, Codex not installed, network_tested=false

python -m threadscout demo
exit 0; explicitly invented HN/Reddit examples
```

Проверены HTML escaping, границы слов, релевантность, URL allowlist, дедупликация, разнообразие веток, skip/snooze, исключение демо, обновление состояния, TTL/tombstones, удаление локального контекста, версии собственного черновика, отмена привязок, Reddit approval gate, mock HN parent/replies/deletion, owner authorization, Mini App HMAC/подмена/давность/другой пользователь, доставка и ошибка доставки с mock Telegram, привязка ответа, копирование, Codex flags/таймаут/отсутствие paid fallback/валидность asset IDs.

## Не выполнено

Живые HN-запросы из приложения: DNS в среде разработки недоступен. Web research выполнен отдельным веб-инструментом; это не end-to-end тест сборщика. Telegram bot token и owner ID не предоставлены. Codex CLI и пользовательская авторизация отсутствуют. Reddit approval/OAuth не предоставлены. HTTPS tunnel и телефон не подключены.

Нет smoke test реального Telegram Bot API, подтверждения текущих CLI-флагов в установке пользователя, live rate-limit теста Reddit, браузерного или Computer Use теста, теста публикации. Отправка на социальные площадки вообще не реализована.

Эти 54 теста — локальная проверка логики с искусственными fixtures и mocks, не доказательство работоспособности внешних сервисов, полного покрытия или готовности к production. Вечерний чек-лист содержит отдельные проверки интеграций.
