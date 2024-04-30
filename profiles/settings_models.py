from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

LOCAL_ENV = "local"


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int

    @property
    def db_connection(self) -> str:
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@"
            f"{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


class RabbitSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    rbtmq_user: str
    rbtmq_pwd: str
    rbtmq_host: str
    rbtmq_worker_port: int
    rbtmq_manager_port: int | None = None
    rbtmq_queue_name: str
    rbtmq_exchange_name: str

    @computed_field
    @property
    def url(self) -> str:
        return f"amqp://{self.rbtmq_user}:{self.rbtmq_pwd}@{self.rbtmq_host}:{self.rbtmq_worker_port}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    env: str
    secret_key: str
    host: str
    cors_origins: list[str] = []
    sentry_dsn: str | None = None
    database: DatabaseSettings

    def is_local_env(self):
        return self.env == LOCAL_ENV
