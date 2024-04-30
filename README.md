# profiles

## Install

```bash
pipx install poetry
poetry install
```

## Development

```bash
# Create .env file
cp example.env .env
# And adjust desired envs

# Start database, rmq, etc.
make run_infra

# And run dev server locally
make run

# Run unit tests
make test

# Generate HTML coverage report and inspect
make coverage

# Run integration tests
make test-integration

# Check and format your code before commit
make lint
make format
```

## Migrations

```bash
# Create new migration
alembic revision --autogenerate -m <migration-verbose-name> --rev-id <ID-of-migration>

# Migrate
make migrate

# Downgrade to specific revision
alembic downgrade 0005
```

## Manual testing

You can use postman for testing your API endpoint. One useful feature is import of service schema using openapi specification.

1. Open postman
2. Click File -> Import
3. Make sure service is running on localhost:8000 (`make run` or `docker compose up`)
4. Enter http://127.0.0.1:8000/openapi.json link and import your collections

After that you can set up different environments and group variables such as JWT and base_url.
JWT can be generated using CLI for existing user.
