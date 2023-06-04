setup:
	pip install --upgrade pip
	pip install -r requirements.txt

format:
	

lint:
	pylint --disable=R,C hello.py

test:
	python -m pytest -vv --cov=hello test_hello.py

all: setup format lint test
