# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние». 
Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть, как реализованы запросы к БД.

Пульт охраны — это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

## Как установить
Для корректной работы приложения необходимо настроить переменные окружения.
Переменные окружения используются для хранения конфиденциальной информации, такой как ключи API, пароли и другие настройки, которые не должны быть жестко закодированы в исходном коде.
Это помогает защитить вашу информацию и упрощает конфигурацию приложения в различных средах (например, разработка, тестирование, продакшен).

### Настройка переменных окружения

1. Создайте файл `.env` в корневой директории проекта.
2. Добавьте необходимые переменные окружения в файл `.env`. Пример содержимого файла:

   `DB_ENGINE=django.db.backends.postgresql_psycopg2` - Эта переменная указывает на тип базы данных, с которой будет работать ваше приложение Django.
Django поддерживает несколько различных баз данных, и для каждой из них есть свой "backend" (драйвер).

   `DB_HOST=your_database_host` - Эта переменная указывает адрес хоста, на котором развернута база данных. Это может быть локальный сервер или удаленный сервер.
В ней вы должны указать IP-адрес или доменное имя сервера базы данных.

   `DB_PORT=5432` - Эта переменная указывает порт, на котором база данных слушает входящие соединения.
Порт — это номер, который используется для идентификации конкретного процесса на сервере.

   `DB_NAME=your_database_name`- Эта переменная указывает имя базы данных, к которой ваше приложение будет подключаться. База данных — это контейнер для хранения данных.
Здесь мы указываем имя базы данных.

   `DB_USER=your_database_user` - Эта переменная указывает имя пользователя, которое будет использоваться для подключения к базе данных. Пользователь должен иметь соответствующие права доступа к базе данных.
   
   `DB_PASSWORD=your_database_password` -  Эта переменная указывает пароль для пользователя базы данных. Пароль необходим для аутентификации пользователя при подключении к базе данных.
   
   `SECRET_KEY=your_secret_key` -Секретный ключ для конкретной установки Django. Он используется для криптографической подписи и должен быть уникальным и непредсказуемым.
   
   `DEBUG=True` - Логическое значение, включающее/выключающее режим отладки.
Если в вашем приложении возникает исключение, когда DEBUG имеет значение True, Django отобразит подробную трассировку,
включая множество метаданных о вашей среде, например, все текущие настройки Django (из файла   `settings.py`).

Эти переменные являются важными настройками для подключения вашего приложения Django к базе данных. 
Правильная конфигурация этих переменных позволяет вашему приложению взаимодействовать с базой данных для хранения и извлечения данных
   
3. Убедитесь, что файл .env добавлен в .gitignore, чтобы избежать случайной утечки конфиденциальной информации.

### Установка зависимостей

Python 3.12.3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python 2) для установки зависимостей:
```python
pip install -r requirements.txt
```
## Цели проекта
Код написан в образовательных целях для онлайн-курса для веб-разработчиков ```dvmn.org.```

