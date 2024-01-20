# PrayerTimesBot

### 1. Create virtual environment and install packages
Windows
```shell
python -m venv venv && venv\bin\activate && pip install -r requirements.txt
```

Linux/Mac
```shell
python3 -m venv venv && source venv/bin/Activate && pip3 install -r requirements.txt
```

### 2. Create .env file and copy all variables from .env_example to it and customize your self (if needed)


### Set Up postgresql

### 1. Install postgresql (if needed)
```shell
sudo apt install -y postgresql postgresql-contrib
```

### 2. Log in to the postgresql shell
```shell
sudo -u postres psql
```

### 3. Create a database (in postgresql shell)
```shell
CREATE DATABASE database_name WITH template = template0 ENCODING 'UTF8' LC_CTYPE 'C' LC_COLLATE 'C';
```

### 4. Create a user (in postgresql shell)
```shell
CREATE USER user_name WITH PASSWORD 'password';
```

### 4. Quit postgresql (in postgresql shell)
```shell
\q
```

### 3. Run app.py
Windows
```shell
python app.py
```

Linux/Mac
```shell
python3 app.py
```

<p align="center">
<br>
<a href="https://www.buymeacoffee.com/anvarbek" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
</p>