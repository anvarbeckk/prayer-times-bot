# PrayerTimesBot

![prayertimebot-ezgif com-optimize](https://github.com/anvarbeckk/prayer-times-bot/assets/121457366/dc720553-d73c-43a7-a427-4b03c04c7308)

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
<a href="https://www.buymeacoffee.com/anvarbek" target="_blank"><img alt="Buy Me A Coffee" height="41" width="174" src="https://github-production-user-asset-6210df.s3.amazonaws.com/73847672/296882953-79a76ef6-a9f8-4c26-bd7d-72bc8048eb25.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240124%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240124T085733Z&X-Amz-Expires=300&X-Amz-Signature=2e7407ceaaeb9e232e1a05141715a15517de10bb01301c1f583d95e77e955d67&X-Amz-SignedHeaders=host&actor_id=121457366&key_id=0&repo_id=690221511"></a>
</p>
