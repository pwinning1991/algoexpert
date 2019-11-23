.PHONY: test localtest

test:
	@pytest

localtest:
	@docker run --rm pwinnington/algoexpert:latest
