# tiktok-amazon-telegram-bot

This bot fetches TikTok videos tagged with `#tiktokmademebuyit`, finds matching
products on Amazon and posts affiliate links to a Telegram channel.

## Installation

1. Install Python 3.9 or later.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in your credentials.


## Usage

Run the bot:
```bash
python main.py
```
The script will scrape TikTok, search Amazon for each product mentioned in a
video and post the information to your Telegram channel.
### Amazon affiliate scraper (Node.js)
Install Node.js and run:
```bash
npm install
node amazon_affiliate_bot.js "trending aesthetic sunset lamp"

```

## Files
- `main.py` – orchestrates scraping and posting
- `tiktok_scraper.py` – retrieves TikTok videos
- `amazon_search.py` – searches Amazon for products
- `telegram_poster.py` – sends messages to Telegram
- `utils.py` – helper functions and environment loading
- `data/used_videos.json` – keeps track of already processed videos
- `deploy.sh` – script to push the project to GitHub

## License

This project is licensed under the MIT License. See `LICENSE` for details.
