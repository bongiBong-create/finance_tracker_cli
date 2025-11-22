from application.get_balance import get_balance

def balance_handler(path, data):
    balance = get_balance(path, data)
    print(f"Баланс: {balance}")

    return True