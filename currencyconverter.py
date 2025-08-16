import requests
import os

# Set your Open Exchange Rates APP ID here (or use environment variable)
APP_ID = os.getenv("OXR_APP_ID", "YOUR_APP_ID_HERE")
BASE_URL = f"https://openexchangerates.org/api/latest.json?app_id={APP_ID}"

def get_rates():
    """Fetch latest exchange rates from Open Exchange Rates API"""
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        data = response.json()
        return data["rates"], data["base"]
    except requests.exceptions.RequestException as e:
        print("Error fetching rates:", e)
        return None, None

def convert_currency(amount, from_currency, to_currency, rates):
    """Convert amount from one currency to another"""
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Invalid currency code.")
    # Convert to base currency (usually USD), then to target
    amount_in_base = amount / rates[from_currency]
    return amount_in_base * rates[to_currency]

def main():
    print("💱 Currency Converter (Python Edition)")
    rates, base = get_rates()
    if not rates:
        print("Could not fetch exchange rates. Try again later.")
        return

    while True:
        try:
            amount = float(input("\nEnter amount: "))
            from_currency = input("From currency (e.g., USD, INR, EUR): ").upper()
            to_currency = input("To currency (e.g., USD, INR, EUR): ").upper()

            result = convert_currency(amount, from_currency, to_currency, rates)
            print(f"\n✅ {amount} {from_currency} = {result:.4f} {to_currency}")

        except ValueError as e:
            print("Error:", e)

        cont = input("\nDo you want another conversion? (y/n): ").strip().lower()
        if cont != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()
