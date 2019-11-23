.PHONY: test localtest

test:
	@pytest

localtest:
	@docker run pwinnington/algoexpert:latest
