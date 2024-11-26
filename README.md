# TopCryptoGainersAndLosersNewsletter

## Description
TopCryptoGainersAndLosersNewsletter is a Python-based application that fetches cryptocurrency data from CoinGecko, retrieves contact details from Google Sheets, and sends daily email notifications.

## Features
- Fetches top cryptocurrency gainers and losers categorized by market cap.
- Dynamically retrieves contact information.
- Sends personalized email notifications.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/TopCryptoGainersAndLosersNewsletter.git
   cd TopCryptoGainersAndLosersNewsletter
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Configure the config.ini file with your email credentials.

4. Set up Google Sheets:
   ```bash
   Share your Google Sheet with the service account email in credentials.json.

5. Run the script:
   ```bash
   python main.py
