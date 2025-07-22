from utils import load_used_videos, save_used_videos
from tiktok_scraper import fetch_videos
from amazon_search import search_product
from telegram_poster import post_to_channel


def main():
    hashtag = 'tiktokmademebuyit'
    used_videos = load_used_videos()
    new_videos = fetch_videos(hashtag, limit=5)

    for video in new_videos:
        product_query = video['desc'][:100]
        product = search_product(product_query)
        if product:
            message = (
                f"{video['url']}\n"
                f"{product['title']}\n"
                f"{product['url']}"
            )
            post_to_channel(message)
            used_videos.add(video['id'])

    save_used_videos(used_videos)


if __name__ == '__main__':
    main()
