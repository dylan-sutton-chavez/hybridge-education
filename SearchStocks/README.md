# Search Stocks

Python web scraping automation using `selenium` to render dynamic java script, with a command-line interface ChatBot Rule-based to search stocks information

## Requirements

- Python 3.9+
- Selenium 4.31.0

`pip install -r requirements.txt`

## Usage

1. Create or download `script.json` archive with something like:

```json
{
  "greeting": "Welcome to this python automation!",
  "response": "{title} → {price} {currency}"
}
```

2. Execute the python script:

`python main.py`

3. Example of usage:

```txt
Welcome to this python automation!

Type the name of your stock (or `exit`): microsoft
Loading...

Microsoft → 426.30 USD
```

## Remember

- The CSS selectors can change if DuckDuckGo change his layout
