#!/usr/bin/env sh

ls -la
pg_restore -O -j 4 -F c -d "$POSTGRES_DB" ./docker-entrypoint-initdb.d/db_dump.psql_dump
