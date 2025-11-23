from application.add_transaction import add_transaction
from datetime import datetime

def add_handler(path, data):
    type_op = input("Введите тип операции: Доход/Расход\n").strip().lower()
    amount = input("Введите сумму\n")
    category = input(f"{'Введите категорию' if type_op == 'доход' else 'Введите покупку'}\n")
    description = input("Введите описание\n")
    date = datetime.now()

    success, error = add_transaction(path, date, type_op, amount, category, description, data)

    if success:
        print("Транзакция успешно добавлена")
    else:
        print(f"Ошибка: {error}")

    return True