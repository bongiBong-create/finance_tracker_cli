from infrastracture.storage import get_data
from infrastracture.storage import save_data

def add_transaction(path, transaction, amount, description):
    data = get_data(path)
    operation = {"type": transaction, "amount": amount, "description": description}
    data.append(operation)
    save_data(path, data)