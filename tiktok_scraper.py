from typing import List, Dict
from TikTokApi import TikTokApi
from utils import load_used_videos


def fetch_videos(hashtag: str, limit: int = 5) -> List[Dict]:
    """Fetch new TikTok videos for the given hashtag."""
    api = TikTokApi()
    used = load_used_videos()
    new_videos = []
    for video in api.hashtag(name=hashtag).videos(count=limit * 2):
        vid = video.as_dict
        vid_id = vid.get('id')
        if vid_id in used:
            continue
        new_videos.append({
            'id': vid_id,
            'desc': vid.get('desc', ''),
            'url': (
                f"https://www.tiktok.com/@{vid.get('author', {}).get('uniqueId')}"
                f"/video/{vid_id}"
            ),
        })
        if len(new_videos) >= limit:
            break
    return new_videos
