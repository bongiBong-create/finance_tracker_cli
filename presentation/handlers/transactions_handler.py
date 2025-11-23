from shared.utils import print_transactions
from application.get_transactions import get_transactions

def transactions_handler(path, data):
    categories = {el["category"] for el in data}
    categories.add("общие")
    category = input(f"Введите категорию: {"/".join(categories)}\n").lower()

    success, error = get_transactions(path, data, category, categories)

    if success:
        print_transactions(success)
    else:
        print(f"{error}")

    return True