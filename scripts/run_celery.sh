#!/bin/sh

# Replace * with name of Django Project
su -m django -c "celery -A config.celery_app worker -l info"