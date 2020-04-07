clean:
	rm -f ./data/*.dat

build:
	docker build . -t agrrh/tg-feed

release: build
	docker push agrrh/tg-feed
