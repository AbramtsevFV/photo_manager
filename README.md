## Фото менеджер
### Запуск Docker ###
- Выполняем команду: 
```
  docker-compose up -d
 ```
### Регистрация
Отправить POST запрос. Пример CURL:

 ```
curl --location --request POST 'http://0.0.0.0:8000/api/v1/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "Fedor",
    "password": "12345678fedor",
    "password2": "12345678fedor",
    "email": "fedor@mail.ru",
    "first_name": "f",
    "last_name": "f"
}'
```
### Аутентификация
 Отправить POST запрос. Пример CURL:

 curl --location --request POST 'http://0.0.0.0:8000/api/v1/login/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "Fedor",
    "password": "12345678fedor",
    "password2": "12345678fedor",
    "email": "fedor@mail.ru",
    "first_name": "f",
    "last_name": "f"
}'
 ```
Ответ, получим JSON с access и refresh токеном:

``
{
    "refresh": "...",
    "access": "..."
}
``
### Работа с фото
Получмть список фотографий пользователя без метаданных:
```curl --location --request GET 'http://0.0.0.0:8000/api/v1/photos/list' \
--header 'Authorization: Bearer token'
```

Получить все фото пользователя. Пример CURL:
```
curl --location --request GET 'http://0.0.0.0:8000/api/v1/photos/' \
--header 'Authorization: Bearer token'

```

 #### Фильтры:
- По дате, параметр date. Пример CURL:
```
    curl --location --request GET 'http://0.0.0.0:8000/api/v1/photos/?date=2022-12-09' \
--header 'Authorization: Bearer token'
```
- По имени человека на фото, параметр name. Пример CURL:
```
curl --location --request GET 'http://0.0.0.0:8000/api/v1/photos/?name=Александр' \
--header 'Authorization: Bearer token'
```
- По геолокации geo_location. Пример CURL:
``curl --location --request GET 'http://0.0.0.0:8000/api/v1/photos/?geo_location=city' \
--header 'Authorization: Bearer token'``

- Получить по id фотографии. Пример CURL:
```
curl --location --request GET 'http://0.0.0.0:8000/api/v1/photo/{id фото}/' \
--header 'Authorization: Bearer token'

```
- Добавить фото. names_of_people - id имени Пример CURL:
    
```
curl --location --request GET 'http://0.0.0.0:8000/api/v1/photos/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwNjA1MjE2LCJpYXQiOjE2NzA2MDQ5MTYsImp0aSI6IjNkNzgxNTkzMWFjNDQ4NDBiYmNjN2FhZTRkMGIwMGFiIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJGZWRvciJ9.RHPjX9xw9M9TP9uI0uL9jeU3UInXeKMSaMVec0V0T2I' \
--form 'photo=@"/home/suvenir/Загрузки/IMG_20211026_093318_186.jpg"' \
--form 'geo_location="city"' \
--form 'description="фото"' \
--form 'names_of_people="43"' \
--form 'names_of_people="44"'
```
### Работа с именами:
- Добавит имя. Пример CURL:
```
curl --location --request POST 'http://0.0.0.0:8000/api/v1/name/' \
--header 'Authorization: Bearer token' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "Александа"}'
```
- Поиск по части имени, параметр name. Пример CURL:
```curl --location --request GET 'http://0.0.0.0:8000/api/v1/name/?name=Алекс' \
--header 'Authorization: Bearer token'```
