from fetch_data import get_gainers_losers_by_market_cap
from fetch_contacts import fetch_contacts
from send_notifications import send_email
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    try:
        # Fetch categorized market cap data
        logging.info("Fetching cryptocurrency data...")
        market_cap_data = get_gainers_losers_by_market_cap()
        logging.info("Fetched cryptocurrency data successfully.")

        # Fetch contacts from Google Sheets
        logging.info("Fetching contacts from Google Sheets...")
        contacts = fetch_contacts()
        logging.info("Fetched contacts successfully.")

        # Prepare email content
        subject = "Daily Crypto Update"
        body = format_email_body(market_cap_data)
        recipients = [contact["email"] for contact in contacts]

        # Send notifications
        logging.info("Sending notifications...")
        send_email(subject, body, recipients)
        logging.info("Notifications sent successfully!")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def format_email_body(market_cap_data):
    """Formats email content with gainers and losers."""
    body = "Daily Cryptocurrency Market Report\n\n"

    for category, data in market_cap_data.items():
        gainers, losers = data
        body += f"=== {category.replace('_', ' ').title()} ===\n"
        body += "Top Gainers:\n"
        for coin in gainers:
            body += (f"- {coin['name']} ({coin['symbol'].upper()}): "
                     f"{coin.get('price_change_percentage_24h', 0):.2f}% "
                     f"Price: ${coin.get('current_price', 0):,.2f}, "
                     f"Volume: ${coin.get('total_volume', 0):,.2f}, "
                     f"Rank: {coin.get('market_cap_rank', 'N/A')}\n")
        body += "\nTop Losers:\n"
        for coin in losers:
            body += (f"- {coin['name']} ({coin['symbol'].upper()}): "
                     f"{coin.get('price_change_percentage_24h', 0):.2f}% "
                     f"Price: ${coin.get('current_price', 0):,.2f}, "
                     f"Volume: ${coin.get('total_volume', 0):,.2f}, "
                     f"Rank: {coin.get('market_cap_rank', 'N/A')}\n")
        body += "\n"

    return body

if __name__ == "__main__":
    main()
