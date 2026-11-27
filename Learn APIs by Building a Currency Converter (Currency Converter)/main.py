# import requests

# url = "https://open.er-api.com/v6/latest/USD"

# response = requests.get(url)

# data = response.json()

# print(response.text)
# print(response.status_code)
# print(data)
# print(data.keys())
# print(data["rates"]["INR"])

# rate = data["rates"]["INR"]


# amount = float(input("Enter the amount in USD: "))
# converted = rate * amount

# print(f"{amount} USD = {converted:.2f} INR")


import requests

while True:
    try:
        # url = "https://open.er-api.com/v6/latest/USD"
        from_code = input("From currency code (e.g. USD): ").upper()
        url = f"https://open.er-api.com/v6/latest/{from_code}"

        response = requests.get(url)

        data = response.json()

        to_code = input("Enter the target currency code (e.g. INR, EUR, JPY): ").upper()

        if to_code not in data["rates"]:
            print("Invalid currency code. Please try again.")
        else:
            rate = data["rates"][to_code]

            # amount = float(input("Enter amount in USD: "))
            amount = float(input("Enter amount: "))
            converted = rate * amount

            # print(f"{amount} USD = {converted:.2f} {to_code}")
            print(f"{amount} {from_code} = {converted:.2f} {to_code}")

    except ValueError:
        print("Please enter a valid number for the amount.")
    except KeyError:
        print("Invalid currency code. Please try again.")
    except Exception as e:
        print("Something went wrong:", e)


    again = input("Do you want to convert another amount? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break
