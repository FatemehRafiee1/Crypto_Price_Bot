# Telegram Crypto Price Bot

This is a Telegram bot written in Python using the aiogram library, designed to provide cryptocurrency information upon user request.

## Features

- Retrieves real-time cryptocurrency data.
- Provides price changes over different time intervals.
- Supports user interaction via commands and inline keyboard.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your system.
- Poetry installed.


## Configuration

1. Create a `config.yaml` file with the following structure:
  ```yaml
  telegram_bot_token: YOUR_TELEGRAM_BOT_TOKEN
  coinex:
    Access_ID: YOUR_COINEX_ACCESS_ID
    Secret_Key: YOUR_COINEX_SECRET_KEY
  ```

2. Replace them with your own tokens.

## Usage

1. Run the script `tgbot.py`:
  ```
  python tgbot.py
  ```
2. Interact with the bot by sending commands or choosing options from the provided menu.

## Available Commands

- `/start`: Displays a welcome message and options menu.
- `/menu`: Displays the available cryptocurrency options.
- User can also type a cryptocurrency symbol directly (e.g., BTCUSDT) after being prompted.

## Note

Contributions are welcome! Feel free to submit any issues or pull requests.

