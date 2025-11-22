def filtered_transactions(transactions, category):
    transactions = [*filter(lambda x: x["category"] == category, transactions)]
    return transactions

def check_length(transactions):
    return True if len(transactions) > 0 else False

def check_index(index):
    return int(index)

def print_transactions(transactions):
    for i, value in enumerate(transactions):
        print(f"Задач №{i + 1}\n"
              f"Тип: {value['type']}\n"
              f"Сумма: {value['amount']}\n"
              f"Категория: {value['category']}")