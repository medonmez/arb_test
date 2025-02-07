# Crypto Arbitrage Telegram Bot

## Project Summary
This bot detects arbitrage opportunities by tracking price differences between Bitci and Binance exchanges and informs users via a Telegram channel.

## Key Features

### 1. Data Collection
- Fetching cryptocurrency pair price data from the Bitci API
- Fetching the same cryptocurrency pair price data from the Binance API
- Data fetching from both exchanges will be repeated at specific intervals (e.g., every 1 minute)

### 2. Data Processing
- Calculating the price differences between the two exchanges
- Detecting differences above a certain percentage (e.g., 1.5%)

### 3. Telegram Integration
- Automatically sending detected arbitrage opportunities as messages to the Telegram channel
- Message format:
  ```
  🔄 Arbitrage Opportunity
  Pair: BTC/USDT
  Bitci: 65,000 USDT
  Binance: 64,000 USDT
  Difference: %1.56 ⬆️
  Date: 12.03.2024 14:30
  ```

## Technical Requirements
- python-telegram-bot library
- requests library (for API requests)
- A continuously running server or host

## Security
- API keys and tokens will be stored as environment variables
- Rate limiting rules will be followed
- Error handling and logging system

## Future Developments
- Adding more exchange markets
- Tracking specific cryptocurrency pairs

## Installation

### 1. Creating a Virtual Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Linux/Mac
source venv/bin/activate
```

### 2. Installing Required Packages
```bash
pip install -r requirements.txt
```

### 3. Setting Up Environment Variables
- Copy the `.env.example` file to `.env`
- Update the variables in the `.env` file with your own values

### 4. Running the Bot
```bash
python main.py
```

### 5. Running Continuously on Server (Linux)
```bash
nohup python main.py &
``` 