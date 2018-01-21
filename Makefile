all: setup

venv/bin/activate:
	virtualenv -p python3 venv; fi

run: venv/bin/activate requirements.txt
	. venv/bin/activate; python3 manage.py runserver

setup: venv/bin/activate requirements.txt
	. venv/bin/activate; pip install -Ur requirements.txt
	. venv/bin/activate; python3 manage.py restore
