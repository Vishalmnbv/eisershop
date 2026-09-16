#!/usr/bin/env bash
set -o errexit

# Upgrade pip and install dependencies explicitly
python -m pip install --upgrade pip
pip install -r requirements.txt

# Run Django commands
python manage.py collectstatic --no-input
python manage.py migrate