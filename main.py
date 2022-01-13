from time import sleep
from currency import Currency


def main():

    print("Welcome to the Currency Exchange!")

    loop = True
    error = None

    while loop:
        currency = Currency()

        print("Checking server message...")
        sleep(2)

        print(f"Connection http respond code: {currency.status()[0]}\nStatus: {currency.status()[1]}")

        q = input("Do you want to Sale, Purchase, or show Currency? (s/p/c): ")

        if q.lower() == 's':
            currency_name = input("Which currency you want to sale?\n(three capital letters): ")
            value = float(input(f"Enter sailing value ({currency_name}): "))
            result = currency.sale(currency_name, value)
            print(f"Result: {result} UAH")

        elif q.lower() == 'p':
            currency_name = input("Which currency you want to purchase?\n(three capital letters): ")
            value = float(input("Enter purchasing value (UAH): "))
            result = currency.sale(currency_name, value)
            print(f"Result: {result} {currency_name}")

        elif q.lower() == 'c':
            currency_name = input("Which currency you want to see?\n(three capital letters): ")
            result = currency.show_currency(currency_name)
            print(f"Result: {result}")

        else:
            print("Wrong letter! Restart...")
            continue

        q = input("Want to restart? (y/n): ")

        if q.lower() == 'y':
            continue
        else:
            loop = False


if __name__ == "__main__":
    main()
