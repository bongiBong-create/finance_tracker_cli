from application.get_transactions import get_transactions
from shared.utils import filtered_transactions, check_length, print_transactions

def transactions_handler(path):
    category = input("Введите категорию: общие и тд.").lower()
    transactions = get_transactions(path)

    if check_length(transactions):
        if category == "общие":
            print_transactions(transactions)
        else:
            transactions = filtered_transactions(get_transactions(path), category)
            if check_length(transactions):
                print_transactions(transactions)
            else:
                print("Нет транзакций этой категории")
    else:
        print("Нет транзакций")

    return True