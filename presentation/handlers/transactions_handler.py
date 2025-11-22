from shared.utils import filtered_transactions, check_length, print_transactions

def transactions_handler(path, data):
    categories = {el["category"] for el in data}
    categories.add("общие")
    category = input(f"Введите категорию: {"/".join(categories)}\n").lower()

    if check_length(data):
        if category in categories:
            if category == "общие":
                print_transactions(data)
            else:
                transactions = filtered_transactions(data, category)
                print_transactions(transactions)
        else:

            print("Нет транзакций этой категории")
    else:
        print("Нет транзакций")

    return True