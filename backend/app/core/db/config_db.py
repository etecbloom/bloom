from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    ECHO: bool = False

    model_config = SettingsConfigDict(
        env_file='.env'
    )

#  https://github.com/pydantic/pydantic/issues/3753
# I had to post this comment because in all my research, 
# the placement settings = Settings() has no solution, only to ignore the error. 
# Apparently, the database connects anyway and it is a Pylance error...
settings = Settings() # pyright: ignore