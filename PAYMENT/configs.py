from dotenv import dotenv_values

venv = dotenv_values(".env")

HOST = venv.get("REDIS_HOST")
PASSWORD = venv.get("REDIS_PASSWORD")
PORT = venv.get("REDIS_PORT")

FRONT_URL = venv.get("FRONT_URL")