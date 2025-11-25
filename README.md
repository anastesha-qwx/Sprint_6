# Sprint_6 — UI-автотесты для Яндекс.Самоката

Проект с автотестами на **Selenium + pytest** по Page Object Model для учебного сервиса «Яндекс.Самокат».

Покрыто:

- FAQ-блок «Вопросы о важном» (выпадающие ответы).
- Позитивное оформление заказа с двумя точками входа.
- Переходы по логотипам Самоката и Яндекса (редирект на Дзен).

---

## Технологии

- **Python 3.х**
- **pytest**
- **Selenium WebDriver**
- **Allure** (allure-pytest)
- **Firefox** + geckodriver

---

## Структура проекта

```text
qa_python_sprint_6/
├── helps/
│   └── data.py              # тестовые данные (пользователи, URL, ответы FAQ)
├── locators/
│   ├── home_page_locators.py  # локаторы главной страницы и хедера
│   ├── order_page_locators.py # локаторы страницы заказа
│   └── dzen_page_locators.py  # локаторы страницы Дзена
├── pages/
│   ├── base_page.py         # базовый Page Object с общими методами
│   ├── home_page.py         # главная страница + хедер
│   ├── order_page.py        # страница оформления заказа
│   └── dzen_page.py         # страница Дзена
├── tests/
│   ├── test_header_page.py  # логотипы, переходы и FAQ
│   └── test_order_page.py   # сценарии оформления заказа
├── allure_results/          # сырые результаты для Allure
├── conftest.py              # фикстура driver (Firefox), базовая настройка pytest
├── requirements.txt         # зависимости проекта
└── README.md
