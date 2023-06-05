install:
	pip install --upgrade pip
	pip install -r requirements.txt

lint:
	pylint --disable=R,C main.py --text "I love this"

test:
	python -m pytest -vv --cov=main test_main.py

