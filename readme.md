Postgres:
    $ sudo -u postgres psql
    postgres=# CREATE DATABASE db_userorders;
    postgres=# CREATE USER db_userorders WITH PASSWORD 'db_userorders_password';
    postgres=# GRANT ALL PRIVILEGES ON DATABASE db_userorders TO db_userorders;          


requirements.txt to env
createsuperuser 


API usage:
http://127.0.0.1:8000/api/users/
http://127.0.0.1:8000/api/users/?date_registration=2018-05-10