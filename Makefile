all: setup

venv/bin/activate:
	virtualenv -p python3 venv

run: venv/bin/activate requirements.txt
	. venv/bin/activate; python3 manage.py runserver

setup: venv/bin/activate requirements.txt
	. venv/bin/activate; pip install -Ur requirements.txt
	. venv/bin/activate; python3 manage.py restore
