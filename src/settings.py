from dotenv import load_dotenv
from environs import Env

load_dotenv()
env = Env()


class Settings:
    WEB3_API_URL = env.str("WEB3_API_URL", "")
    HTTP_TIMEOUT = env.int("HTTP_TIMEOUT", 6)
    MAX_CONNECTIONS = env.int("MAX_CONNECTIONS", 100)
    MAX_KEEPALIVE_CONNECTIONS = env.int("MAX_KEEPALIVE_CONNECTIONS", 20)
    KEEPALIVE_EXPIRY = env.int("KEEPALIVE_EXPIRY", 1800)
