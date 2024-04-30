from loguru import logger
from pydantic_core import ValidationError

import profiles.settings_models as settings_models

try:
    settings = settings_models.Settings(
        database=settings_models.DatabaseSettings(),
    )
except ValidationError as e:
    logger.critical("Some environment variables are missing or invalid!")

    for env_error in e.errors():
        env_name = env_error["loc"][0]
        logger.critical(f"{env_name}: {env_error['msg']}")

    raise e
