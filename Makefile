init:
	pip install -r requirements.txt

test:
	py.test tests

run:
	python setup.py start

.PHONY: init test
