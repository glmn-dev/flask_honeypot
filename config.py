import os


def cast_bool(value: str) -> bool:
    if not value:
        return False
    return value.lower() in ("true", "t", "1", "yes")


class Config(object):
    SECRET_KEY: str = os.environ.get('SECRET_KEY') or 'honey-pot-web-app'
    HOST: str = os.environ.get('HP_HOST')
    PORT: int = os.environ.get('HP_PORT') or 5000
    TG_API_KEY: str = os.environ.get('TG_API_KEY')
    TG_ADMIN: int = os.environ.get('TG_ADMIN')
    TG_REPORTS: bool = cast_bool(os.environ.get('TG_REPORTS'))
    DEBUG: bool = cast_bool(os.environ.get('DEBUG'))
