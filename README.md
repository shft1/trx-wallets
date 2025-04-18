# Trx-Wallets

### Подготовка к запуску проекта:

**Клонируйте репозиторий:**

```
git@github.com:shft1/trx-wallets.git
```

**Создайте и активируйте виртуальное окружение:**

```
python3 -m venv venv
```

- _Если у вас Linux/macOS_
  ```
  source venv/bin/activate
  ```
- _Если у вас Windows_
  ```
  source venv/scripts/activate
  ```

**Установите зависимости из файла requirements.txt:**

```
pip install -r requirements.txt
```

**Заполните файл .env в корне проекта:**

```
DATABASE_URL - адрес БД SQLite
API_KEY_TRON - API-ключ к TronGrid
```

**Выполните запуск тестов для проверки корректности работы приложения:**

```
pytest
```

**Результат выполнения тестов**:

