import os
from dotenv import load_dotenv


load_dotenv()

HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))             
bootstrap_servers = os.getenv("BOOTSTRAP_SERVER")
# bootstrap_servers = os.getenv("DOCKER_BOOTSTRAP_SERVER")
# bootstrap_servers = os.getenv("AWS_BOOTSTRAP_SERVER")

