account_balance = 500
def withdraw_money(amount):
    try:
        if amount > account_balance:
            raise ValueError("Not enough money!")
    except ValueError as e:
               print(f"❌ Transaction Failed: {e}")

withdraw_money(1000)

        