import json
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DATA_PATH = Path('data')
USED_VIDEOS_FILE = DATA_PATH / 'used_videos.json'


def get_env_var(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise EnvironmentError(f"Environment variable {name} not set")
    return value


def load_used_videos(path: Path = USED_VIDEOS_FILE) -> set:
    if not path.exists():
        return set()
    with open(path, 'r') as f:
        try:
            data = json.load(f)
            return set(data)
        except json.JSONDecodeError:
            return set()


def save_used_videos(video_ids: set, path: Path = USED_VIDEOS_FILE) -> None:
    DATA_PATH.mkdir(exist_ok=True)
    with open(path, 'w') as f:
        json.dump(list(video_ids), f, indent=2)
