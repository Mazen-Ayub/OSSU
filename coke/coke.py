def main():
    # Define accepted coin denominations and the price of a Coke
    coin_denominations = [25, 10, 5]
    coke_price = 50

    # Initialize variables
    insert_coin = 0

    # Prompt the user to insert coins until enough money is inserted
    while insert_coin < coke_price:
        # Inform the user of the amount due
        amount_due = coke_price - insert_coin
        print(f"Amount Due: {amount_due}")

        # Accept user input (coin)
        coin = int(input("Insert Coin: "))

        # Check if the coin is a valid denomination
        if coin in coin_denominations:
            insert_coin += coin
        else:
            print("Amount Due: ")

    # Calculate change
    change_owed = insert_coin - coke_price

    # Output the change owed to the user
    print(f"Change Owed: {change_owed}")


if __name__ == "__main__":
    main()
