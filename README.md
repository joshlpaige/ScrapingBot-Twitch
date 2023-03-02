# Twitch to YouTube Bot

Automatically make video compilations of the most viewed Twitch clips, and upload them to YouTube using Python 3.

## Usage

Example of running with only default values:

```text
python main.py
```

[`config.py`](twitchbot/config.py):

```python
DATA = ["channel maskenissen"]

CLIENT_ID = "1hq8ektpki36w5kn37mluioungyqjo"  # Twitch Client ID
OAUTH_TOKEN = "9f5einm9qtp0bj4m9l1ykevpwdn98o"  # Twitch OAuth Token
PERIOD = 24  # day, week, month or all
LANGUAGE = "en"  # en, es, th etc.
LIMIT = 100  # 1-100
...
```

## Installation

To install all the packages needed, you have to run this command, by being in the same directory as the `requirements.txt` and `main.py` files are.

```
pip install -r requirements.txt
```
