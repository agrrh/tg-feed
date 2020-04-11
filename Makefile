clean:
	docker rm -f tg-feed || true
	sudo find ./storage/* ! -path .gitstore -delete || true

build: clean
	docker build . -t agrrh/tg-feed

build_noclean:
	docker build . -t agrrh/tg-feed

release: build
	docker push agrrh/tg-feed

run: build_noclean
	docker run \
		--rm -ti --name tg-feed \
		-v $$(pwd)/config.yml:/app/config.yml \
		-v $$(pwd)/storage:/app/storage \
		agrrh/tg-feed
