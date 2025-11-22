from application.get_balance import get_balance

def balance_handler(path):
    balance = get_balance(path)
    print(f"Баланс: {balance}")

    return True