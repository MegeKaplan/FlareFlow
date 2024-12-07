from dotenv import load_dotenv
import os
import requests
from .db import get_db_connection

load_dotenv()

flare_api_url = os.getenv("FLARE_API_URL")

db = get_db_connection()


def add_image_to_post(post_id, image_url):
    try:
        cursor = db.cursor()
        sql = "INSERT INTO `post_images` (`post_id`, `image_url`) VALUES (%s, %s)"
        values = (
            post_id,
            image_url,
        )
        cursor.execute(sql, values)
        db.commit()
    except Exception as e:
        print(e)


def create_post(post_data, image_url, token):
    try:
        response = requests.post(
            f"{flare_api_url}/posts",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            },
            json=post_data,
        )
        data = response.json()
        post_id = data["response"]
        add_image_to_post(post_id, image_url)
        return data
    except Exception as e:
        print(e)
