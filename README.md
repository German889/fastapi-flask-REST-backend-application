# Тестовое задание backend-разработчика
Решение включает в себя 3 отдельных приложения:
1) fastapi Сервис, который принимает HTTP запросы с указанием кадастрового номера, широты и долготы, отправляет запрос с этими данными на внешний сервер, сохраняет сами данные запроса и результат обработки (ответ) внешнего сервера в локальную базу данных. Сервис поддерживает несколько видов запросов:
   - "/query" - для передачи кадастрового номера, широты и долготы на внешний сервер, с сохранением их и ответа в базе
   - "/result" - для получения списка всех координат по переданному кадастровому номеру
   - "/ping" - проверка, что внешний сервер работает
   - "/history" - получение истории запросов и ответов внешнего сервера
   - "/docs" - документация к API, автоматически сгенерированная fastapi
   - "/admin/queries/" - админ-панель с таблицей из базы
2) fastapi Сервис, симулирующий работу "внешнего сервера". Принимает запросы от основного, возвращает ответ со случайной задержкой (имитация обработки данных)
3) flask Админ-панель базы данных. Графический интерфейс, который позволяет просматривать и изменять данные в базе.

тесты функционала проводились в Postman, можно открыть их в браузере
[https://www.postman.com/giver899/workspace/test-task](url)