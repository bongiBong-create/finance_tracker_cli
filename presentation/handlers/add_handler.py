from datetime import datetime
from presentation.handlers.config import incomes, expenditure
from application.add_transaction import add_transaction

def add_handler(path, data):
    type_op = input(f"Введите тип операции: {incomes}/{expenditure}\n").strip().lower()
    amount = input("Введите сумму\n")
    category = input(f"{'Введите категорию' if type_op == incomes else 'Введите покупку'}\n")
    description = input("Введите описание\n")
    date = datetime.now()

    success, error = add_transaction(path, date, type_op, amount, category, description, data)

    if success:
        print("Транзакция успешно добавлена")
    else:
        print(f"Ошибка: {error}")

    return True