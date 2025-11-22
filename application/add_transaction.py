from infrastracture.storage import get_data
from infrastracture.storage import save_data

def add_transaction(path, transaction, amount, category):
    data = get_data(path)
    operation = {"type": transaction, "amount": amount, "category": category}
    data.append(operation)
    save_data(path, data)