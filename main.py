import schedule
from time import sleep
from utils import fetch_news, login_to_flare, create_post, add_image_to_post
from dotenv import load_dotenv
import os

load_dotenv()

flare_bot_account_id = os.getenv("FLARE_BOT_ACCOUNT_ID")


def job():
    news_list = fetch_news()

    token = login_to_flare()

    for news in news_list:
        if "image" in news:
            post_data = {
                "content": news["description"],
                "sender_id": 1,
            }
            create_post(post_data, news["image"], token)
    print("Job Done!")


def main():
    job()

    schedule.every(1).days.do(job)

    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == "__main__":
    main()
