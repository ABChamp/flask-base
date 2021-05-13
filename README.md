# Install on local development on windows
> 1 Install python and virtual env
```
$virtualenv venv
$venv\Scripts\activate
$pip install -r requirements.txt
```
> 2 Run
```
set FLASK_APP=app/app/main.py
set FLASK_DEBUG=1
flask run --port=8000
```