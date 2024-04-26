all: testall

LOCKFILE=/tmp/up.run
PULL=missing

testall:
	for i in tests/*.py; do \
	  python $$i; \
	done

test:
	python $(FILE)

up: $(LOCKFILE)

down:
	docker compose -p test down --rmi local
	make clean

$(LOCKFILE):
	docker compose -p test -f compose.yml -f compose_test.yml up --pull $(PULL) --quiet-pull -d | tee $(LOCKFILE)
	sleep 5

clean:
	rm -f $(LOCKFILE)


testall_in_docker: up
	docker compose -p test exec -w /workspaces web make testall
	make down

test_in_docker: up
	docker compose -p test exec -w /workspaces web make test FILE=$(FILE)
	make down



