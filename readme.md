# JrachkaTop
####
### Я не зовсім зрозумів текст:
```
Якщо чеки для цього замовлення
вже були створені
 – повертає помилку (передається номер замовлення)
```
### Тому зробив трохи по своему
Зберігаю в редісі кєш запиту, і якщо один і той самий Юзер робить один і той самий запит в період кілько секунд, то буде повертати 409 та інформацю про замовлення

Для асинхронних задач обрав `Celery`
####
# Deploy
Щоб запустити проэкт
`./build.sh`
скрипт запустить необхідні докер контейнери
####
Далі треба запустити сам Джанго, запустивши стандартно через пайтон менедж дот пай
####
Можна і через `gunicorn JrachkaTop.wsgi`
####
Підключив сваггер, він доступний тут:
[/api/v1/swagger/](http://127.0.0.1:8000/api/v1/swagger/)
####
Щоб авторизуватися в свагері треба додати `Bearer <token>`
#### Example:
```
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjczMTAyMTM2LCJpYXQiOjE2NzMwMTU3MzYsImp0aSI6IjMyYWU3MDA1MTQ5NTRmYTViMmNhMDM4NDhlZTE3NDkwIiwidXNlcl9pZCI6MX0.oVh2i1-kx03gKcMmModO9fBYkIZY9S7aDfEPGZCxPDo
```
