from application.add_transaction import add_transaction

def add_handler(path):
    transaction = input("Введите тип операции: Доход/Расход\n").strip().lower()
    if transaction == "доход":
        amount = int(input("Введите сумму\n"))
        category = input("Вид заработка\n")

        add_transaction(path, transaction, amount, category)
        print("Транзакция успешно добавлена")
    elif transaction == "расход":
        amount = int(input("Введите сумму\n"))
        category = input("Введите покупку\n")

        add_transaction(path, transaction, amount, category)
        print("Транзакция успешно добавлена")
    else:
        print("Введите корректную операцию")

    return True