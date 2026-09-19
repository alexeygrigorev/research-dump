# Lightning Lessons: 10 идей, 4 выбранных эфира

Подготовлено 18 сентября 2026. Это предложения для публикации, не созданные на Maven или в календаре мероприятия. Все времена — Europe/Berlin; на этих датах UTC+2. Основная кампания начинается 28 сентября.

## 1. Десять тем

| № | Тема | Практическая демонстрация | Артефакт | Решение |
|---|---|---|---|---|
| 1 | AI делает не то: преврати идею в понятное ТЗ | Расплывчатая идея → пользователь, сценарий, ограничения и критерии готовности | Одностраничная спецификация | Эфир 1 |
| 2 | Первый экран готов. Как перестать переписывать приложение и закончить его | Маленькие задачи, сохранение контекста и независимая проверка AI-изменений | Рабочий цикл task → change → test | Пост / короткое видео |
| 3 | Выведи AI-проект из localhost | Подготовленное приложение → публикация → проверка основного сценария | Checklist первого деплоя | Эфир 2 |
| 4 | Урежь MVP: один работающий сценарий вместо двадцати функций | Разобрать перегруженный backlog и исключить лишнее | In scope / out of scope | Пост / упражнение |
| 5 | Преврати README в понятную страницу продукта | Переписать описание с языка технологий на язык пользователя | README и план демонстрации | Пост / часть набора |
| 6 | Сделай приложение понятным без твоих объяснений | Наблюдать первое использование без подсказок разработчика | Сценарий теста и приоритеты | Эфир 3 |
| 7 | Добавь три события и узнай, где теряются пользователи | Начало, ключевое действие, завершение одного сценария | Мини-план аналитики | Пост / фрагмент курса |
| 8 | Преврати отзыв пользователя в следующий полезный коммит | Отделить симптом от проблемы, сформулировать задачу, проверить исправление | Feedback-to-change template | Пост / гостевая тема |
| 9 | Найди первых тестировщиков, даже когда у тебя нет аудитории | Выбрать подходящее сообщество и сделать конкретный запрос | План поиска и приглашение | Пост / гостевая тема |
| 10 | Покажи свой AI-проект: живой разбор с Алексеем | Разобрать 2–3 присланных продукта и следующий шаг для каждого | Заполненный лист ревью | Эфир 4 |

Последовательность: постановка задачи → публикация → пользователь → разбор. Последний эфир показывает личную помощь, которая входит в платный курс.

## 2. Календарь

| Дата | Время | Английское название |
|---|---|---|
| Четверг, 1 октября 2026 | 18:30–19:15 | Turn an Idea into an AI-Ready Spec |
| Четверг, 8 октября 2026 | 18:30–19:15 | Take Your AI App Beyond Localhost |
| Вторник, 13 октября 2026 | 18:30–19:15 | Make Your App Ready for Real Users |
| Четверг, 15 октября 2026 | 18:30–19:30 | Get Your AI Project Reviewed Live |

Окна 18:15–19:45 ранее проверены в доступных календарях; перед созданием событий перепроверить. Две встречи на последней неделе — компромисс перед периодом недоступности преподавателя, не постоянный ритм. Для первого эфира только три дня продвижения: объявить все четыре даты 28 сентября и ориентировать первый на знакомую аудиторию.

## 3. Общие правила

Одна предметная область на всю серию: небольшой инструмент для организации учебных групп или другое уже существующее приложение. Не строить четыре разных demo. Подготовка включает рабочую ветку, тестовые данные, сохранённый исправный commit, отдельное demo-окружение и короткую резервную запись.

Участник должен получать пользу без покупки курса. Оставить коммерческому переходу 2–3 минуты, а не превращать половину урока в презентацию оффера. Использовать разные понятные CTA по этапам кампании. Все ссылки ниже в квадратных скобках необходимо заменить фактическими URL.

Maven описывает Lightning Lessons как бесплатные короткие live-занятия. Для гостевых записей использовать честную маркировку recorded interview; не объявлять премьеру записи живым уроком. См. [документацию Maven](https://help.maven.com/en/articles/14559254-growing-your-audience-on-maven).

## 4. Эфир 1 — Turn an Idea into an AI-Ready Spec

**Дата:** 1 октября, 18:30–19:15. **Цель:** привлечь аудиторию AI Dev Tools и дать первый небольшой результат.

### Готовая копия для Maven — English

**Title:** Turn an Idea into an AI-Ready Spec

**Subtitle:** Stop asking AI to build “an app.” Give it one useful user flow and a definition of done.

**Description:**

You ask a coding agent to build your idea. It produces a convincing screen, but important details are missing—or it solves a different problem.

In this live lesson, I’ll take one rough product idea and turn it into a short specification we can actually build from. We’ll define the user, choose the core flow, remove unnecessary features, and write acceptance criteria before generating more code.

You’ll leave with a reusable one-page template and a worked example. Bring a small project idea, or follow along with mine. This session is useful whether you are building a tool for your work, your community, or a small product of your own.

**What you’ll learn:**

- Turn a broad idea into one concrete user job and a small first version.
- Tell a coding agent what to build, what not to build, and what “done” means.
- Check the plan before spending time on implementation.

**Who this is for:** People who have tried AI coding tools and want a clearer way to begin their own project. No finished application is required for this lesson.

**Takeaway:** An AI-ready product brief and a completed example from the session.

**CTA:** Register for the free lesson.

### Сценарий на 45 минут

0–5: показать неудачное расплывчатое задание и его недостатки. 5–12: определить пользователя и один сценарий. 12–23: заполнить спецификацию и убрать лишние функции. 23–32: попросить AI составить план и проверить его по критериям. 32–41: вопросы / один краткий пример аудитории. 41–45: материал, следующий эфир и короткое объяснение курса.

**Подготовить:** заполненный пример и пустой бланк из [lead-magnets.md](lead-magnets.md). **После эфира:** добавить пример в набор №1, отправить запись и ссылку на урок №2.

## 5. Эфир 2 — Take Your AI App Beyond Localhost

**Дата:** 8 октября, 18:30–19:15. **Цель:** показать доступный результат и открыть набор.

### Готовая копия для Maven — English

**Title:** Take Your AI App Beyond Localhost

**Subtitle:** Turn a local demo into a link someone else can open and use.

**Description:**

Your AI-built app works on your computer. Before you send it to someone else, there is another step: making sure the deployed version works for a new user, not just for you.

I’ll use a prepared application to demonstrate a first deployment and a practical smoke test. We’ll check configuration, open the app in a clean browser session, and walk through the main user flow. I’ll also show how to isolate a deployment problem without asking the agent to rewrite everything.

This is a focused walkthrough, not a promise to build an entire full-stack product from scratch in 45 minutes. You can apply the same checklist to a project you already have.

**What you’ll learn:**

- Identify the minimum work needed to publish one working end-to-end flow.
- Check a deployed app from a new user’s perspective.
- Diagnose a failed step and make a small, verifiable fix.

**Takeaway:** A first-deployment checklist and a worked example.

**Who this is for:** People with a local prototype, or learners who want to understand the step between generated code and a usable link.

**CTA:** Register for the free lesson.

### Сценарий

0–5: показать готовый сценарий и границы demo. 5–15: конфигурация и публикация подготовленного приложения. 15–28: проверка в чистом браузере, тестовые данные, основной путь. 28–34: одна заранее воспроизводимая проблема и её диагностика. 34–41: вопросы. 41–45: checklist и открытие набора на Product Shipping.

Не вводить production-секреты на общем экране. Не обещать одинаковый деплой на всех платформах. Не превращать инфраструктуру в главную тему курса.

**После эфира:** дополнить набор №1, открыть форму подачи проектов на 15 октября, отправить письмо об открытии набора с точными датами курса и каникул.

## 6. Эфир 3 — Make Your App Ready for Real Users

**Дата:** 13 октября, 18:30–19:15. **Цель:** перейти от кода к понятности и реальной проверке.

### Готовая копия для Maven — English

**Title:** Make Your App Ready for Real Users

**Subtitle:** Find out what breaks when you stop explaining your product.

**Description:**

You know where to click because you built the app. A new user does not.

In this practical session, we’ll look at an app without the developer’s running commentary. Can someone understand what it does, start the main task, complete it, and tell us what went wrong?

I’ll demonstrate a short first-use test, separate observations from assumptions, and turn the findings into a small list of improvements. The goal is not to add more features. It is to make the existing product easier to understand and use.

**What you’ll learn:**

- Run a short user test without leading the participant toward the answer.
- Check the first screen, main flow, error states, and feedback path.
- Choose the next three improvements instead of collecting an endless feature backlog.

**Takeaway:** A first-user test script and the project review worksheet I use in live reviews.

**Who this is for:** Builders with a working prototype and people preparing to share a project for the first time.

**CTA:** Register for the free lesson.

### Сценарий

0–5: правила теста и знакомство с задачей. 5–18: новый пользователь проходит основной сценарий без подсказок. 18–28: разобрать наблюдения, отличить неудобство от запроса новой функции. 28–35: выбрать три следующих изменения. 35–42: вопросы. 42–45: материал, подача проекта и приглашение на живой разбор.

Нужен тестировщик, заранее согласившийся на запись, но не отрепетировавший ответы. В резерве допустима запись реального теста, явно обозначенная как запись. Не инсценировать её как первое использование.

**После эфира:** отправить набор №2, напомнить о дедлайне подачи 14 октября. Объяснить, что личные разборы всех представленных проектов предусмотрены на платном курсе, а бесплатный эфир ограничен выбранными примерами.

## 7. Эфир 4 — Get Your AI Project Reviewed Live

**Дата:** 15 октября, 18:30–19:30. **Цель:** показать работу Алексея с конкретными продуктами и сообществом.

### Готовая копия для Maven — English

**Title:** Get Your AI Project Reviewed Live

**Subtitle:** Watch real project reviews and leave with a clearer next step for your own app.

**Description:**

Have you built something with AI but are not sure what to improve next?

In this live session, I’ll review two or three projects submitted by the community. We’ll look at the intended user, the first-use experience, the main workflow, and the gap between “it runs” and “someone can use it.” For each project, we’ll choose a concrete next step.

You can learn from the reviews even without submitting a project. We’ll use the same worksheet throughout, so you can apply the questions to your own app afterward.

**What you’ll learn:**

- Identify the most important problem in a working prototype.
- Separate essential fixes from attractive but unnecessary features.
- Turn product feedback into a focused next iteration.

**Project submissions:** Submit a working demo link and a short description by October 14. We will select a small number of projects for this free session. Submitting does not guarantee a live review. Only submit work you have permission to show publicly.

**Takeaway:** A reusable review worksheet and worked examples from the session.

**CTA:** Register to watch the reviews. Submit a project here: [PROJECT_FORM_URL].

### Сценарий на 60 минут

0–5: рамка и критерии. 5–47: три разбора по 14 минут, либо два более глубоких. 47–55: повторяющиеся закономерности и вопросы. 55–60: как устроены два проектных этапа и личные разборы на курсе.

Приглашённый эксперт может выступить вторым рецензентом, но исходный эфир должен состояться без него. Не публиковать имя гостя до подтверждения.

### Минимальная форма подачи

Название проекта; для кого он; основной пользовательский сценарий; доступная ссылка; бесплатные безопасные инструкции тестирования; что сейчас непонятно автору; разрешение на публичный показ и запись; отдельное разрешение на короткие промофрагменты. Не просить production-пароли или частные данные пользователей.

## 8. Общая короткая биография для страниц уроков — English

Alexey Grigorev is the founder of DataTalks.Club, creator of the Zoomcamp series, and author of Machine Learning Bookcamp. He teaches practical, project-based AI and software development and uses AI in his own education and community workflows.

Биографическая основа: [существующая страница Buildcamp](https://maven.com/alexey-grigorev/from-rag-to-agents) и [Business Operating System](https://maven.com/alexey-grigorev/ai-native-business-operating-system). Не переносить отзывы и рейтинг другого курса как отзывы нового.

## 9. Чеклист после каждого эфира

Сохранить запись и ссылки на рабочие материалы; проверить согласия на публичные фрагменты; извлечь один конкретный вывод и два коротких видео; обновить уже существующий downloadable; отправить одно релевантное письмо вместо повторов; исключить записавшихся на платный курс из лишних продающих напоминаний.
