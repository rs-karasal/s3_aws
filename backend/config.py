import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_ENDPOINT_URL = os.getenv("AWS_ENDPOINT_URL")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")
