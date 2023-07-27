# praktikum_new_diplom
# Развернутый проект доступен по ссылке:
# http://51.250.31.157/redoc/
# http://51.250.31.157/admin/
# LOGIN : admin1
# EMAIL : admin1@mmail.ru
# PASS  : admin1

# foodgram
[![Workflow Status](https://github.com/user-user2023/foodgram-project-react/actions/workflows/main.yml/badge.svg)](https://github.com/user-user2023/yamdb_final/actions/workflows/main.yml)

# Продуктовый помощник
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