def currency_converter():
 exchange_rates = {
        "USD": 1.0,    
        "EUR": 0.85,   
        "GBP": 0.75,   
        "INR": 74.0,   
        "JPY": 110.0   
    }
 while True:
  print(" :: Currency Converter :: ")
  amount = float(input("Enter the amount: $"))
  from_currency = input("Enter the currency (USD, EUR, GBP, INR, JPY)")
  to_currency = input("Enter the currency to convert to (USD, EUR, GBP, INR,JPY)")
  if from_currency not  in exchange_rates or to_currency not in exchange_rates:
   print("Invalid currency")
   return
  convert_USD = amount/exchange_rates[from_currency]
  covert_amount = convert_USD * exchange_rates[to_currency]
  print(f"{amount} {from_currency} is equal to {covert_amount:.2f} {to_currency}")

if __name__ == "__main__":
 currency_converter()