# PicassoSoft

* **

* ### Запуск проекта
    * Установить python версии 3.6 или выше
    * Установить необходимыве пакеты из файла requirements.txt. (Желательно активировать окружение)
    Для этого необходимо выполнить команду pip install requirements.txt в терминале.
      (Находиться в папке с файлом requirements.txt)
    * Установить Базу данных Postgreql.
    * Создать новую БД
    * в файле merchandiser/merchandiser/settings.py в переменной DATABASES проверить все данные подключения к БД.
    * Перейдите в каталог где находится файл manage.py и выполните следующие команды
      * Применить sql скрипт к базе.
      * загрузить данные в бд при помощи команды python manage.py import_csv <Путь к csv файлу>
      * python manage.py migrate ( для применения миграций БД )
      * python manage.py runserver ( для запуска проета в локальной среде )

* ### URL
  
  |   URL | Описание                                                   |
  |------------------------------------------------------------| ------ |
  | api/v1/police-orders/ | query параметрами являются limit, offset, date_from, date_to |