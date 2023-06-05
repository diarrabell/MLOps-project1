install:
	pip install --upgrade pip
	pip install -r requirements.txt

lint:
	pylint --disable=R,C library/model.py --text "I love this"

test:
	python -m pytest -vv --cov=main test_main.py

