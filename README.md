# TechStore UI Automation Framework

Навчальний фреймворк для E2E-тестування процесу покупки на [Swag Labs](https://www.saucedemo.com/) із використанням Python, Selenium WebDriver, Pytest, Page Object Model (POM) та Allure Reports.

## Структура проєкту

```text
project2/
├── pages/                  # Page Objects та BasePage
├── tests/                  # E2E-тести
├── utils/                  # Допоміжні функції та тестові дані
├── reports/                # Результати Allure
├── conftest.py             # Pytest fixtures та WebDriver
├── pytest.ini              # Конфігурація Pytest і Allure
├── requirements.txt        # Залежності Python
├── Dockerfile              # Конфігурація Docker-образу
├── .gitignore              # Файли, виключені з Git
└── README.md               # Документація проєкту
```

## Технології

- **Python** — мова програмування.
- **Selenium WebDriver** — автоматизація браузера.
- **Pytest** — запуск і організація тестів.
- **Page Object Model (POM)** — організація взаємодії зі сторінками.
- **Allure Reports** — формування тестових звітів.
- **Docker** — запуск тестів у контейнеризованому середовищі.

## Вимоги

Для локального запуску потрібні:

- Python 3.10 або новіший.
- Google Chrome.
- Сумісний ChromeDriver.
- Allure CLI — для перегляду HTML-звіту.

Для запуску в контейнері потрібен Docker Desktop або інше робоче Docker-середовище. У Docker-образі встановлюються Chromium і ChromeDriver, тому окремо встановлювати браузер на хост-системі не потрібно.

## Встановлення та запуск на macOS

### 1. Створення віртуального середовища

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Встановлення залежностей

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3. Запуск тестів

Якщо Selenium Manager автоматично знаходить сумісний ChromeDriver:

```bash
python -m pytest
```

Якщо Selenium Manager не може знайти драйвер, укажіть шлях до встановленого ChromeDriver:

```bash
CHROMEDRIVER="$HOME/chromedriver/chromedriver-mac-arm64/chromedriver" python -m pytest
```

За замовчуванням браузер запускається в headless-режимі.

Щоб запустити тест із видимим вікном браузера:

```bash
HEADLESS=false CHROMEDRIVER="$HOME/chromedriver/chromedriver-mac-arm64/chromedriver" python -m pytest
```

Результати тестування зберігаються в `reports/allure-results/`.

## Allure Reports

Allure використовується для формування звітів про виконання тестів.

Для встановлення Allure CLI на macOS через Homebrew:

```bash
brew install allure
```

Після запуску тестів відкрий звіт командою:

```bash
allure serve reports/allure-results
```

Allure згенерує звіт і відкриє його в браузері. Для подання лабораторної роботи за потреби зроби скриншот звіту з результатами тестування.

## Запуск через Docker

### 1. Створення Docker-образу

Виконай команду в кореневій папці проєкту:

```bash
docker build -t techstore-ui-tests .
```

### 2. Запуск автотестів у контейнері

```bash
docker run --rm -v "$(pwd)/reports:/app/reports" techstore-ui-tests
```

Docker-образ містить Python, Chromium, ChromeDriver і залежності з `requirements.txt`. Тести запускаються в headless-режимі.

Параметр `--rm` автоматично видаляє контейнер після завершення роботи. Підключений том зберігає результати Allure у локальній папці `reports/`.

## E2E-сценарій покупки

Тест `test_buying_process` перевіряє основний процес покупки на Swag Labs:

1. Відкриття сайту та вхід під користувачем `standard_user`.
2. Додавання товару `Sauce Labs Backpack` до кошика.
3. Перевірка товару в кошику.
4. Заповнення даних оформлення замовлення.
5. Підтвердження покупки.
6. Перевірка повідомлення `Thank you for your order!`.

## Архітектура тестового фреймворку

- **BasePage** інкапсулює базові операції взаємодії з вебелементами та явні очікування.
- **Page Objects** містять локатори й методи для взаємодії зі сторінками сайту.
- **conftest.py** створює WebDriver через Pytest fixture та закриває браузер після тесту.
- **Pytest** керує запуском тестів і налаштуваннями через `pytest.ini`.
- **Allure** зберігає результати виконання для подальшого формування звіту.
- **Docker** забезпечує запуск тестів в ізольованому середовищі.

Для синхронізації з вебсторінками використовуються явні очікування замість `time.sleep()`.

## Результати тестування

Тестовий сценарій було успішно виконано:

- Локально — **1 passed**.
- У Docker-контейнері — **1 passed**.

Результати Allure зберігаються в `reports/allure-results/`. Тимчасові файли, кеші, віртуальне середовище та згенеровані звіти виключаються з Git відповідно до `.gitignore`.

## Примітки

- Перед локальним запуском переконайся, що встановлено сумісні версії Python, Google Chrome та ChromeDriver.
- Для Docker достатньо встановленого й запущеного Docker Engine.
- Для перегляду HTML-звіту потрібен Allure CLI.
