def filtered_transactions(transactions, category):
    return [el for el in transactions if el["category"] == category]

def check_length(transactions):
    return bool(transactions)

def check_index(index, data):
    return 0 <= int(index) < len(data)

def print_transactions(transactions):
    for i, value in enumerate(transactions):
        print(f"Транзакция №{i + 1}\n"
              f"Время и дата: {value['date']}\n"
              f"Тип: {value['type']}\n"
              f"Сумма: {value['amount']}\n"
              f"Категория: {value['category']}\n"
              f"Описание: {value['description']}")

def get_datetime(date, flag=None):
    time = date.time().strftime("%H:%M")
    date = date.date()
    y, d, m = date.year, date.month, date.day

    if flag == "дата":
        return f"{d}.{m}.{y}"
    elif flag == "время":
        return time

    return f"{d}.{m}.{y} {time}"