run:
	docker compose --verbose up --remove-orphans --force-recreate

sh-head:
	docker exec -it ray_head bash

sh-worker:
	docker exec -it ray_worker bash

sh-client:
	docker exec -it ray_client bash
