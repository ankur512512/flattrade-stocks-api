# flattrade-stocks-api
API usage for flattrade

## Pre-requisites:

- python version: Python 3.11.5

As of now, only below works:

1. Get the token using userid, password, totp (needs to be refreshed daily)
2. Web-socket (still needs to be tested)

## Usage (Windows)

### Setup the virtual environment first:

```bash
git clone https://github.com/ankur512512/flattrade-stocks-api.git
cd flattrade-stocks-api
python3 -m venv venv
venv\Scripts\activate
```

### Install libraries & export the env vars:
```bash
pip install -r requirements.txt
# Replace with actual values
set userid=FT1234
set password=mypassword
set totp=totpkey
set api_key=apikey
set api_secret=apisecret
```

### Run code:

```bash
python socket_streaming.py
```

## Usage (Linux)

### Setup the virtual environment first:

```bash
git clone https://github.com/ankur512512/flattrade-stocks-api.git
cd flattrade-stocks-api
python3 -m venv venv
source venv/bin/activate
```

### Install libraries & export the env vars:
```bash
pip install -r requirements.txt
# Replace with actual values
export userid=FT1234
export password=mypassword
export totp=totpkey
export api_key=apikey
export api_secret=apisecret
```

### Run code:

```bash
python socket_streaming.py
```