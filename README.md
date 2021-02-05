# Проект: «Проект 42. Мобильное приложение»

Группа, ответственная за backend для приложения.

Ссылка на сайт для проекта: http://pd-2020-2.std-881.ist.mospolytech.ru/
Ссылка на отчетный матерьял: https://drive.google.com/drive/u/0/folders/1DH6fsIko4Qp953tdNfAN5vTZ1Ayj-45v

## Задачи на проект

## Участники

| Учебная группа | Имя пользователя | ФИО                      | Роль                       |
|----------------|------------------|--------------------------|----------------------------|
| 181-352        | @Facassanxt      | Стебло А.С.              | Разработчик django сервера |
| 181-352        | @TimurChikishev  | Чикишев Т.В.             | Разработчик django сервера |

## Личный вклад участников

### Стебло А.С. 
- Ознакомился с работой прошлой команды - 5 часа
- Ознакомился с использованием Django и Django REST, ORM Django, структурой проекта  Django - 10 часов
- Помощь с реализацией API - 5 часов
- Работа со Swagger API Documentation - 30 часов
  - Использование drf-yasg в качестве автоматического генератора Swagger из API Django Rest Framework
- Помощь Системному Администратору - 5 часов
- Реализация сайта для проекта - 5 часов
- Исправление багов - 8 часов
- Тестирование API - 5 часов
- Составление "Комплект отчётных материалов (Отчёт,Видеопрезентация,Промо видео,Презентация в формате PDF)" - 10 часов
####        Общий объем работы оценивается в 83 - часа
------------------------------
### Чикишев Т.В.
- Ознакомился с работой прошлой команды - 5 часа
- Поставил и настроил centos 8 на VirtualBox (т.к. вся разработка будет под эту ОС) - 3 часа
- Ознакомился с использованием Django и Django REST, ORM Django, структурой проекта  Django - 10 часов
- Настроил виртуальное окружение: - 10 часов
  - Установил postgresql-13 
  - Установил и настроил pgadmin4
  - Создал и настроил django api server
  - Настроил сбор логов (state: [debug, info])
- Реализация API - 30 часов
  - Создал множество get запросов (пример: получение списка пользователей, редактирование пользователей...)
  - Столкнулся с проблемой расширения основного класса User 
    - В результате исселедования принял решение создать модель профиля с помощью связи один-к-одному
  - Для авторизации использовал библиотеку djoiser
    - Взял ее т.к. по требованию мобильных разработчиков нужен было токен.
      djoiser позволяет работать с несколькими видами токенов одновременно.
  - Для регистрации возникла потребность автоматически добавлять данные в таблицу профиля
  - Реализовал кастомные сообщения о ошибках
  - Добавил разграничение доступа
  - Внедрение Swagger
- Исправление/Реализация API чата - 10 часов
  - Иправил представленный макет api
  - Автоматизировал добавление всех возможных атрибудтов на стороне сервера
- Постер для проекта - 1 час
- Исправление багов - 5 часов
- Составление "Комплект отчётных материалов (Отчёт,Видеопрезентация,Промо видео,Презентация в формате PDF)" - 10 часов
####        Общий объем работы оценивается в 84 - часа 
------------------------------
