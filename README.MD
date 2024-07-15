## Описание проекта

Проект представляет собой API для мобильного приложения, в котором полевой сотрудник заказчика будет выполнять визиты в магазины. API позволяет:

- Получить список торговых точек, привязанных к работнику по номеру телефона.
- Зарегистрировать посещение торговой точки.

## Требования

- Python 3.8+
- Django 4.2
- Django REST Framework
- PostgreSQL

## Установка и запуск проекта

### 1. Клонирование репозитория

```bash
git clone https://github.com/ArtyomBatmanov/test_task_avtomatika.git
cd mysite
```


### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Нсстройка базы данных

Установите PostgreSQL, если он еще не установлен:
```bash
sudo apt install postgresql postgresql-contrib
```

Запустите и настройте PostgreSQL:
```bash
sudo systemctl start postgresql
sudo systemctl enable postgresql

```

Создайте базу данных и пользователя:
```bash

sudo -i -u postgres
psql
CREATE DATABASE mysite_db;
CREATE USER admin WITH PASSWORD 'admin';
\q
exit
```


### 4. Настройка переменных окружения

Создайте файл .env в корне проекта по примеру файла .env.template



### 5. Применение миграций и создание тестовых данных


```bash
python manage.py makemigrations
python manage.py migrate
python manage.py create_test_data

```



### 6. Запуск сервера



```bash
python manage.py runserver

```


