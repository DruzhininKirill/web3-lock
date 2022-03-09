#!/bin/bash
set -e
if [ -z "$NO_MIGRATION" ]; then
    echo "Applying migrations"
    pipenv run alembic upgrade head
    echo "Done"
fi

echo "Starting application"
exec "$@"
