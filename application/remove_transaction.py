from infrastracture.storage import get_data
from infrastracture.storage import save_data

def remove_transaction(path, index):
    transactions = get_data(path)

    if 0 <= index < len(transactions):
        transactions.pop(index)
        save_data(path, transactions)
        return True

    return False