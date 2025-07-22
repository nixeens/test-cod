from telegram import Bot
from utils import get_env_var


def post_to_channel(message: str) -> None:
    bot = Bot(token=get_env_var('TELEGRAM_TOKEN'))
    chat_id = get_env_var('TELEGRAM_CHAT_ID')
    bot.send_message(chat_id=chat_id, text=message)
