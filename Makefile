clean:
	rm -f ./data/*.dat
	docker rm -f tg-feed

build:
	docker build . -t agrrh/tg-feed

release: build
	docker push agrrh/tg-feed

run: build
	docker run \
		--rm -d --name tg-feed \
		-v $$(pwd)/data:/app/data \
		-v $$(pwd)/config.yml:/app/config.yml \
		agrrh/tg-feed
