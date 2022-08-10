# Zample

## Installation guide

### 1) Initialize Backend
`$ cd backend`<br>
`$ pyenv virtualenv 3.9.0 zample`<br>
`$ pyenv activate zample`<br>
`$ pip install -r requirements.txt`<br>

#### For mac users only if you get an ssl error instaling psycopg2:
`$ env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2`


### 2) Adds .env file like:
`$ touch .env`

DB_NAME=zample<br>
DB_USER=zample<br>
DB_PASSWORD=1234<br>
DB_HOST=127.0.0.1<br>
DB_PORT=5432<br>


### 3) Create DataBase

`$ sudo psql -U {username} postgres`<br>
`$ CREATE USER zample WITH PASSWORD '1234';`<br>
`$ ALTER USER zample CREATEDB;`<br>
`$ \q`<br>

`$ sudo psql -U zample postgres`<br>
`$ CREATE DATABASE zample OWNER zample;`<br>
`$ \q`<br>


### 4) Run migrations

`python manage.py migrate`<br>
