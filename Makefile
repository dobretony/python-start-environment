init:
	pip install -r requirements.txt

test:
	py.test tests

run:
	cd app; echo ""; \
	scrapy crawl example

.PHONY: init test
