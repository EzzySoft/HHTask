## Описание

Использовал NoSQL  [MongoDB](https://www.mongodb.com/)

При помощи `.env` файла можно указать название и локальный url базы данных - `MONGO_INITDB_DATABASE`,`MONGO_URI`. По
умолчанию для локальной разработки - `mongodb://localhost:27017/task`

>[Postman Collection](https://www.postman.com/betabooking/workspace/hh-task/request/17664279-f8db0142-dcaf-4d88-811d-2a731a3aba5a)

>[DockerHub url](https://hub.docker.com/r/ezzysoft/hh-task)



## Запуск
Запустить используя образ из DockerHub:
```bash
docker compose up
```



>При изменении `.env` файла необходимо собрать образ локально 
>```bash
>docker compose up --build
>```


