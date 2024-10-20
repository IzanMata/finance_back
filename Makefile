# Define variables
PYTHON = python3
DJANGO_MANAGE = $(PYTHON) manage.py
VENV = env

# Targets
.PHONY: all install migrate run shell test lint type-check clean

all: install

install:
	$(PYTHON) -m venv $(VENV)
	. $(VENV)/bin/activate && pip install -r requirements.txt

migrate:
	. $(VENV)/bin/activate && $(DJANGO_MANAGE) migrate

run:
	. $(VENV)/bin/activate && $(DJANGO_MANAGE) runserver

shell:
	. $(VENV)/bin/activate && $(DJANGO_MANAGE) shell

test:
	. $(VENV)/bin/activate && $(DJANGO_MANAGE) test

lint:
	. $(VENV)/bin/activate && flake8 personal_finance
	. $(VENV)/bin/activate && pylint personal_finance **/*.py

type-check:
	. $(VENV)/bin/activate && mypy personal_finance

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	rm -rf $(VENV)
