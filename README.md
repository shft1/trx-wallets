# Trx-Wallets

### Описание
Проект Trx-Wallets представляет собой API для работы с блокчейном TRON 

---

### Подготовка к запуску проекта:

**Клонируйте репозиторий:**

```
git clone git@github.com:shft1/trx-wallets.git
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

**Выполните миграции:**

```
alembic upgrade head
```

**Выполните запуск тестов для проверки корректности работы приложения:**

```
pytest
```

**Результат выполнения тестов**:

<img width="1239" alt="image" src="https://github.com/user-attachments/assets/eeb42bed-5142-4bb6-b4c5-65647fe6fe04" />

---

### Запуск приложения

**Выполните запуск веб-сервера:**

```
uvicorn app.main:app --reload
```

**Интерактивная документация находится по адресу:**

```
http://127.0.0.1:8000/docs#/
```

