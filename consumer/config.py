import os
from dotenv import load_dotenv


load_dotenv()

HOST = os.getenv("MongoHOST")
BOOTSTRAP_SERVER = os.getenv("BOOTSTRAP_SERVER")
# BOOTSTRAP_SERVER = os.getenv("DOCKER_BOOTSTRAP_SERVER")
# BOOTSTRAP_SERVER = os.getenv("AWS_BOOTSTRAP_SERVER")