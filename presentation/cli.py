from application.add_transaction import add_transaction
from application.get_transactions import get_transactions
from application.remove_transaction import remove_transaction
from application.get_balance import get_balance
from infrastracture.storage import init_path
from infrastracture.storage import init_storage


def start_cli():
    path = init_path()
    init_storage(path)

    while True:
        command = input("Введите команду: Добавить/Удалить/Баланс/Операции/Выход\n").lower()

        match command:
            case "добавить":
                transaction = input("Введите тип операции: Доход/Расход\n").strip().lower()
                if transaction == "доход":
                    amount = int(input("Введите сумму\n"))
                    description = input("Вид заработка\n")
                    add_transaction(path, transaction, amount, description)
                    print("Транзакция успешно добавлена")
                elif transaction == "расход":
                    amount = int(input("Введите сумму\n"))
                    description = input("Введите покупку\n")
                    add_transaction(path, transaction, amount, description)
                    print("Транзакция успешно добавлена")
                else:
                    print("Введите корректную операцию")
            case "баланс":
                balance = get_balance(path)

                print(f"Баланс: {balance}")
            case "операции":
                transactions = get_transactions(path)
                if len(transactions) > 0:
                    for i, value in enumerate(transactions):
                        print(f"Задач №{i + 1}\n"
                              f"Тип: {value['type']}\n"
                              f"Описание: {value['description']}")
                else:
                    print("Нет транзакций")
            case "удалить":
                index = int(input("Введите номер транзакции"))
                remove_transaction(path, index - 1)
                print("Транзакция успешна удалена")
            case "выход":
                break
            case _:
                print("Введите корректную команду")

start_cli()