init:
	pip install -r requirements.txt

test:
	py.test tests

run:
	export FLASK_APP=app
	export FLASK_ENV=development
	flask run

.PHONY: init test
