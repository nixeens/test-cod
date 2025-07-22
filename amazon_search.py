from typing import Optional, Dict
from amazon_paapi import AmazonApi
from utils import get_env_var


def get_amazon_client() -> AmazonApi:
    return AmazonApi(
        get_env_var('AMAZON_ACCESS_KEY'),
        get_env_var('AMAZON_SECRET_KEY'),
        get_env_var('AMAZON_TAG'),
        country='US'
    )


def search_product(query: str) -> Optional[Dict]:
    api = get_amazon_client()
    items = api.search_items(keywords=query, search_index='All', item_count=1)
    if items.items:
        item = items.items[0]
        return {
            'title': item.item_info.title.display_value,
            'url': item.detail_page_url,
        }
    return None
