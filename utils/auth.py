from dotenv import load_dotenv
import requests
import os

load_dotenv()

flare_api_url = os.getenv("FLARE_API_URL")
flare_bot_email = os.getenv("FLARE_BOT_EMAIL")
flare_bot_password = os.getenv("FLARE_BOT_PASSWORD")

params = {"country": "tr", "tag": "general"}
headers = {"content-type": "application/json"}


def login_to_flare(email=flare_bot_email, password=flare_bot_password):
    try:
        response = requests.post(
            f"{flare_api_url}/auth/login",
            headers={
                "Content-Type": "application/json",
            },
            json={"email": email, "password": password},
        )
        data = response.json()
        token = data["response"]["token"]
        return token
    except Exception as e:
        print(e)
