from dotenv import load_dotenv
from pydantic import SecretStr
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    bot_token: SecretStr

    postgres_db: str
    postgres_user: str
    postgres_password: SecretStr
    postgres_url: str

    redis_host: str
    redis_port: str
    redis_db: str
    # redis_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Config()
