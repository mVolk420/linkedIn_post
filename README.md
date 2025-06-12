# LinkedIn Posting Automation

This small project automates the process of publishing short LinkedIn posts and
automatically sends connection requests to grow your network. It collects
recent IT related news articles, asks OpenAI's API to generate a short post and
then publishes it using Selenium.

## Requirements

- Python 3.9 or higher
- Safari WebDriver (for macOS) or a Selenium driver of your choice
- A LinkedIn account
- An OpenAI API key


## Installation

1. Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install the Python dependencies manually:

```bash
pip install openai python-dotenv selenium feedparser
```

3. Create a `.env` file in the project root with the following entries:

```ini
EMAIL=your_linked_in_email
PASSWORD=your_linked_in_password
OPENAI_API_KEY=your_openai_key
```

## Usage

Run the main script:

```bash
python main.py
```

The script fetches a few IT related headlines via Google News, generates a
LinkedIn post text with OpenAI and publishes the post through Selenium. It then
tries to connect with up to 100 suggested contacts.

Please use this responsibly and be aware of LinkedIn's terms of service when
using automation.

