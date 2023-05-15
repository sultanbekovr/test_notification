#!/bin/sh

su -m django -c "celery -A config.celery_app worker --beat --scheduler django --loglevel=info --pidfile="