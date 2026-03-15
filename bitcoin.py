import requests
import sys

try:
    if len(sys.argv)==1:
        sys.exit("Missing command-line argument")
    else:
        n=float(sys.argv[1])
    response=requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=93282b78aada5d7f76cfb772863398a9e1bd91648c74b4636cf2d5200da7fd80")
    s=response.json()
    price=float(s["data"]["priceUsd"])
    cost=n*price
    print(f"$ {cost:,.4f}")

except requests.RequestException:
    print("error")
except ValueError:
    sys.exit("Command-line argument is not a number")


