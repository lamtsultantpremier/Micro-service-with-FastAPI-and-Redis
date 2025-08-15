from dotenv import dotenv_values

venv = dotenv_values(".env")

HOST = venv.get("REDIS_HOST")
PORT = venv.get("REDIS_PORT")
PASSWORD = venv.get("REDIS_PASSWORD")
FRONT_URL = venv.get("FRONT_URL")