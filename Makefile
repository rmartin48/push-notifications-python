# Makefile for pusher_push_notifications
all: run

rebuild_venv:
	rm -rf venv
	make venv

venv:
	test -d venv || python3 -m virtualenv venv
	venv/bin/pip3 install -Ur requirements.txt
	venv/bin/pip3 install -Ur dev_requirements.txt

run: venv
	@echo "Running pusher_push_notifications..."

check: test

test: venv
	@venv/bin/python3 -m nose -s

lint: venv
	@venv/bin/python3 -m pylint ./pusher_push_notifications/*.py
