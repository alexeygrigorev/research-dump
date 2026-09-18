# Downloadables: два выбранных набора и четыре варианта переиспользования

Подготовлено 18 сентября 2026. Здесь находятся план упаковки, готовые тексты страниц и редактируемые шаблоны. Финальные файлы для выдачи, регистрационные страницы и рассылки ещё не опубликованы. Полный набор из 28 оригинальных промптов следует собрать из указанного собственного материала, а не считать этот документ его копией.

## 1. Четыре идеи с минимальной новой работой

| Вариант | Существующая основа | Минимальная дополнительная работа | Решение |
|---|---|---|---|
| From Idea to Production: Working Kit | Статья Алексея от 28 августа 2026 с 28 промптами, стадиями Build / Deploy / Operate | Убрать оформление рассылки, добавить отметки результата и короткий product brief | Набор №1 |
| Is Your Project Ready for Its First Users? | Критерии midterm и вопросы ревьюерам из Product Shipping | Короткая проверка, сценарий теста, лист приоритетов, один заполненный пример | Набор №2 |
| README & Demo Kit | Статья How to Write a Good README от 16 июля 2026 | Шаблон README, пример до/после и план двухминутного demo | Запасной вариант; часть включить в набор №2 |
| One-Page MVP Brief | JTBD, аудитория, scope и сценарий первого модуля | Один бланк и один пример | Включить в набор №1, не делать отдельную кампанию |

Исходники:

- [From Idea to Production in 28 Prompts — опубликованная статья](https://aishippingblog.com/p/from-idea-to-production)
- [Тот же текст в Telegram Writing Assistant](https://github.com/alexeygrigorev/telegram-writing-assistant/blob/master/reference/substack/2026-08-28-from-idea-to-production.md)
- [How to Write a Good README — архив исходного текста](https://github.com/alexeygrigorev/telegram-writing-assistant/blob/master/reference/substack/2026-07-16-how-to-write-a-good-readme.md)
- [Product Shipping — программа и критерии проектов](https://github.com/alexeygrigorev/telegram-writing-assistant/blob/master/articles/datatalksclub/product-shipping-zoomcamp.md)

## 2. Набор №1 — From Idea to Production: Working Kit

**Когда:** первая версия 28 сентября; дополнения после уроков 1 и 8 октября. **Задача:** дать существующей технической аудитории удобный способ применить знакомый материал к своему проекту.

Минимальный состав: `prompts.md` с исходными 28 шагами; `product-brief.md`; `progress.md` с колонками «результат / проверка / ссылка»; короткий `deployment-checklist.md`. Достаточно Markdown и одного простого printable-файла при необходимости; сложная упаковка, отдельный сайт и новая большая книга не нужны.

**Редакторская проверка перед выдачей:** в исходной статье пример начинается с инструмента для учебных групп, а следующий frontend-промпт упоминает system design interview application. При переупаковке привести демонстрацию к одной предметной области. Проверить нумерацию всех 28 шагов, ссылки, используемый стек и актуальность команд. Не переносить старые инструкции без пробного прохода.

### Copy for the opt-in page — English

**Title:** From Idea to Production: The AI Builder’s Working Kit

**Subtitle:** Turn a useful idea into a sequence of small, testable steps.

**Description:** Get the working version of my 28-prompt build, deploy, and operate guide: a one-page product brief, a progress tracker, and a checklist for sharing your first deployed version. Use the templates with your own coding assistant and project.

This is a structured starting point, not a guarantee that every generated change is correct. You remain responsible for reviewing the output, protecting secrets, and checking the deployed app.

**What’s inside:** The original prompt sequence in a convenient working format; an editable MVP brief; a result-and-verification tracker; and the deployment checks used in the live lesson series.

**Button:** Get the working kit

**Delivery note:** I’ll email you the kit and updates about the free lessons and Product Shipping with AI. You can unsubscribe at any time.

Editorial note: publish the promise of the original prompt sequence only once the complete file has been assembled. Keep the original article publicly accessible; the email offer adds convenience and worked examples.

### Delivery email — English

**Subject:** Your AI Builder’s Working Kit

Here is the kit: [DOWNLOAD_URL].

Start with the one-page product brief. Choose one user, one useful task, and one result you can test. Then use the prompt sequence in small steps, recording what you checked after each one.

The free lesson series shows the same process in practice: [SERIES_URL].

Alexey

### Editable template: product-brief.md

```markdown
# One-page product brief

## Who is this for?
A specific person or group:

## What job are they trying to do?
When ___, I want to ___, so that ___.

## What evidence do I have?
Observed problem / conversation / example:
Source or notes:
What is still an assumption:

## One core user flow
1. The user starts by:
2. They provide or choose:
3. The product helps them:
4. They know it worked when:

## First version
Must include:
Explicitly excluded:

## Acceptance checks
- [ ] A new user can start without the developer explaining the app.
- [ ] The core task can be completed with test data.
- [ ] Failure produces an understandable message.
- [ ] The deployed version is accessible to an invited tester.

## First people to ask
Where the intended users already spend time:
How I can respectfully request a test:

## Constraints
Time available:
Tool / hosting budget:
Data or access restrictions:

## What would change my mind?
Evidence that this scope or idea needs to change:
```

### Editable template: progress.md

```markdown
# Build progress

| Step | Intended result | What I changed | How I checked it | Evidence / URL | Next action |
|---|---|---|---|---|---|
| Scope | One useful flow | | | | |
| Build | Thin working slice | | | | |
| Test | Main flow verified | | | | |
| Deploy | Accessible URL | | | | |
| First user | Observed attempt | | | | |
| Improve | One justified change | | | | |

Before accepting an AI-generated change:
- Read the relevant diff and identify new dependencies.
- Run the appropriate tests and try the main user flow.
- Check that secrets and private data are not exposed.
- Keep a known-good version and a way to undo the change.
```

## 3. Набор №2 — Is Your Project Ready for Its First Users?

**Когда:** 12 октября базовая версия; 16 октября добавить разрешённый пример с эфира. **Задача:** показать пользу личного разбора и помочь самостоятельно обнаружить самые важные проблемы.

Состав: checklist первого использования, сценарий короткого теста, лист ревью и приоритизации. Никакой большой теории. Для коммерческих продуктов предусмотреть безопасный бесплатный путь тестирования; не просить ревьюеров платить.

### Copy for the opt-in page — English

**Title:** Is Your Project Ready for Its First Users?

**Subtitle:** The practical worksheet I use to review AI-built projects.

**Description:** Your app runs. Can someone else understand what it does and complete the main task without your help?

Use this kit to check the first-use experience, run a short user test, and choose your next improvements. It includes a review checklist, a test script, and a simple way to separate essential fixes from features that can wait.

**What’s inside:** First-use and access checks; an observation-first test script; a structured project review; and a fix-now / later / not-doing decision sheet.

**Button:** Get the project review kit

**Delivery note:** I’ll email you the kit and updates about project reviews, free lessons, and Product Shipping with AI. You can unsubscribe at any time.

### Delivery email — English

**Subject:** Your project review kit

Here is the worksheet: [DOWNLOAD_URL].

Open your deployed app in a clean browser session and try the checklist. Then ask one person to attempt the main task while you observe without coaching them.

Do not turn every comment into a new feature. Start with the problem that prevents the main task from working.

You can see the worksheet in action here: [REVIEW_SESSION_OR_RECORDING_URL].

Alexey

### Editable template: first-user-review.md

```markdown
# First-user project review

Project:
Intended user:
Core task:
Deployed URL:
Date / version:
Reviewer:

## Access and clarity
- [ ] I can open the app from a clean browser session.
- [ ] I can test the relevant flow without paying.
- [ ] I understand who the product is for and what it helps them do.
- [ ] The first action is clear.
- [ ] Demo data is safe and does not expose real user information.

## Main flow
- [ ] I can start the task.
- [ ] I can complete it.
- [ ] I can recognize a successful result.
- [ ] Loading and error states are understandable.
- [ ] I know what to do next or how to get help.

## Observations, not guesses
What I tried:
What I expected:
What actually happened:
Where I hesitated:
What the developer had to explain:

## Product feedback
What worked well:
The most important obstacle:
What I would change first:
What should not distract the builder yet:

## Next iteration
| Observation | Proposed change | Why now? | How to test the change |
|---|---|---|---|
| | | | |

Fix now:
Consider later:
Do not do, and why:
```

### Editable template: short-user-test.md

```markdown
# Short user test

Before the session:
- Ask permission for notes; ask separately before recording or publishing.
- Use safe test data and provide access without payment.
- Describe the task, not the exact buttons to press.

Opening:
“I’m testing the product, not you. Please say what you are trying to do.
I may stay quiet so I can see where the interface is unclear.”

Task:
“You want to ___. Please try to do that using this app.”

Observe:
Where do they start?
Where do they hesitate?
Can they finish?
What did they think the result meant?

Follow-up:
What did you expect this product to help with?
What was most confusing?
How do you handle this task today?
What would need to change before you used it again?

Afterward:
One observed problem:
One assumption still untested:
One next change:
One way to check whether that change helped:
```

## 4. Как материалы рождаются из эфиров и интервью

| Источник | Что сохраняем | Куда добавляем |
|---|---|---|
| Урок 1: спецификация | Заполненный product brief | Набор №1 |
| Урок 2: деплой | Проверки и разбор одной ошибки | Набор №1 |
| Урок 3: тестирование | Наблюдения и приоритетный список | Набор №2 |
| Урок 4: проекты | Один заполненный лист с разрешения автора | Набор №2 |
| Интервью с техническим экспертом | Его проверка задачи / результата, согласованная к публикации | Набор №1 или №2, не новый большой продукт |
| Интервью о контенте | Пример «build notes → launch post», без выдуманных метрик | Дополнительная страница в существующем наборе |

Не выдавать шаблон, пересказанный по интервью, за авторский материал гостя без согласования. Ссылаться на гостя и оригинал. Отдельно уточнить разрешение на включение материалов в платный курс.

## 5. Выпуск без лишней работы

Сначала рабочий Markdown и заполненный пример; затем простая упаковка. Проверить доступ из приватного окна, фактическую выдачу файла и корректность ссылки в письме. Никаких опубликованных токенов, реальных паролей или персональных данных тестировщиков. Показатели чужого продукта использовать только с разрешения.

Не путать «подготовлен текст страницы» и «настроена система подписки». Для запуска нужны опубликованный файл, форма, понятное согласие на письма и проверенный путь от регистрации до получения материала.
