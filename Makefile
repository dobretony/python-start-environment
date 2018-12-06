init:
	pip install -r requirements.txt

test:
	py.test tests

run:
	python3 setup.py start

.PHONY: init test
