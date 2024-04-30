FROM python:3.11-slim

WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN apt-get update && apt-get install -y --no-install-recommends make curl && apt-get clean

RUN pip install --no-cache-dir poetry==1.8.2
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-root

COPY profiles1 ./

EXPOSE 8000

ENTRYPOINT ["poetry", "run"]
CMD ["uvicorn", "profiles.main:app", "--host", "0.0.0.0", "--port", "8000"]
