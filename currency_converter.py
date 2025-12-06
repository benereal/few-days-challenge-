import argparse
parser = argparse.ArgumentParser(description="Currency Converter CLI Tool")
parser.add_argument("--amount", type=float, help="Amount to convert")
parser.add_argument("--from_currency", type=str, help="Original currency code")
parser.add_argument("--to_currency", type=str, help="Target currency code")

args = parser.parse_args()
def my_currency(amount, from_currency, to_currency):
    rates = {
        "USD": 1,
        "EUR": 0.92,
        "NGN": 780,
        "GBP": 0.81,
        "JPY": 150
    }
    try:
        if from_currency in rates and to_currency in rates:
            convert= rates[to_currency] / rates[from_currency] * amount
            convert=round(convert, 2)
            return convert
        if from_currency not in rates :
            print( f"Unsupported currency: {from_currency}")
        if to_currency not in rates :
            # print( f"Unsupported currency: {to_currency}")
            return "Conversion not supported yet."
    except ZeroDivisionError as e:
        pass

result = my_currency(args.amount, args.from_currency, args.to_currency)
print(f"Converted Amount from: {args.amount} to", result)