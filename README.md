# Message Counter

Message Counter is a Python-based Discord bot that tracks and counts messages sent by users in a server. It also provides basic analytics, such as identifying when messages are most frequently sent.

## Installation

1. Download or clone the repository.
2. Set up the bot on a local machine or a hosting service such as **bot-hosting.net**.
3. Open `main.py` and replace the placeholder value for `BOT_TOKEN` with your Discord bot token.
4. Install the required dependencies and start the bot.

## Usage

Run the following commands in a Discord server where the bot is installed:

### `/getMessageCounts [server_id]`

Collects message counts from the specified server and saves the data to a JSON file for later analysis.

### `/msgcounts`

Displays message counts grouped by channels within the server, allowing users to see which channels are the most active and least active

### `/getTrendGraph me|all`

Generates a weekly message activity trend graph for either:

- `me` — your own message activity
- `all` — the entire server's message activity

## Hosting

The bot is designed to run continuously and is currently hosted on **bot-hosting.net**.

## Data Collection

The bot logs message activity to a local JSON file. For each message, it records the timestamp, including both the date and time. This data can be analyzed later using tools such as **Pandas**, **SQL**, or other data analysis frameworks to gain insights into server activity and messaging patterns.

## Features

- See the server's and you own weekly message trends
- Track message counts per channel
- Export message statistics to JSON
- Generate weekly message activity trend graphs
- Store timestamped message data for custom analytics

## Notes

- The bot requires the appropriate Discord permissions to read messages and generate statistics.
- Message data is stored locally on the host machine.
- Be sure to comply with Discord's Terms of Service and your server's privacy policies when collecting and analyzing message data.
