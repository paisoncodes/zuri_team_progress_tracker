import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
import environ

env = environ.Env()
environ.Env.read_env()

cloudinary.config(
    cloud_name=os.getenv("cloud_name"),
    api_key=os.getenv("api_key"),
    api_secret=os.getenv("api_secret"),
)


def upload_image(image):
    upload_data = cloudinary.uploader.upload(image)
    print(upload_data)
    return upload_data["url"]
