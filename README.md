# praktikum_new_diplom
# Развернутый проект доступен по ссылке:
# http://51.250.31.157/recipes/
# http://51.250.31.157/admin/
# foodgram
[![Workflow Status](https://github.com/user-user2023/foodgram-project-react/actions/workflows/main.yml/badge.svg)](https://github.com/user-user2023/foodgram-project-react/actions/workflows/main.yml)

# Дипломный проект <<Продуктовый помощник>>
На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Инструкции по установке

Клонировать репозиторий:

```
git clone https://github.com/user-user2023/foodgram-project-react/
```
Запустить Docker

Из папки infra запустить docker-compose.yaml:
```
docker-compose up
```

Команда для пересборки контейнеов:
```
docker-compose up -d --build
```
Применить миграции:

```
docker-compose exec web python manage.py migrate
```

Создать суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```

Собрать статику:
```
docker-compose exec web python manage.py collectstatic --no-input 
```


## Запустить проект локально:
Клонировать репозиторий:

```
git clone https://github.com/user-user2023/foodgram-project-react/
```
Создать и активировать виртуальное окружение:
```
py -3.9 -m venv venv
```
Обновить pip и установить зависимости
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Применить миграции и выгрузить данные ингредиентов в базу
```
python manage.py migrate
python manage.py import_ingredients_csv
python manage.py load_tags
```
Запустить проект
```
python manage.py runserver
```

## **Actions secrets**
```
MY_KEY
DB_ENGINE
DB_NAME
POSTGRES_USER
POSTGRES_PASSWORD
DB_HOST
DB_PORT
DOCKER_PASSWORD
DOCKER_USERNAME
HOST
PASSPHRASE
POSTGRES_PASSWORD
POSTGRES_USER
SSH_KEY
USER
```
## Страницы доступные на сай
Проект развернут в Docker контейнерах nginx, PostgreSQL и Django. На сервере в Яндекс.Облако. Доступен по адресу: http://51.250.31.157/recipes

## Разработчик:
Анатолий Левченко
