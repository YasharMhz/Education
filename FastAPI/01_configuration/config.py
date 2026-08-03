from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    project_name: str
    version: str
    debug: bool


    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
settings = get_settings()
# class Settings(BaseSettings):
#     app_name: str
#     debug: bool
#     database_url: str
#     secret_key: str
#
#     class Config:
#         env_file = ".env"
#
# @lru_cache
# def get_settings():
#     return Settings()
#
#
# settings = get_settings()