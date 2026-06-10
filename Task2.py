# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_investment = 0

print("Available Stocks:")
for stock in stock_prices:
    print(stock)

try:
    num_stocks = int(input("\nHow many different stocks do you own? "))

    for i in range(num_stocks):
        stock_name = input("\nEnter stock name: ").upper().strip()

        if stock_name in stock_prices:
            quantity = int(input("Enter quantity: "))

            investment = stock_prices[stock_name] * quantity
            total_investment += investment

        else:
            print("Stock not found!")

    print("\nTotal Investment Value: $", total_investment)

    with open("portfolio.txt", "w") as file:
        file.write("Total Investment Value: $" + str(total_investment))

    print("Result saved in portfolio.txt")

except ValueError:
    print("Please enter valid numbers only!")