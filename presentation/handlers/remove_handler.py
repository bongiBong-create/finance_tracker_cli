from application.remove_transaction import remove_transaction

def remove_handler(path):
    try:
        index = int(input("Введите номер транзакции\n"))
        flag = remove_transaction(path, index - 1)

        if flag:
            print("Транзакция успешна удалена")
        else:
            print("Такой транзакции не существует")
    except ValueError:
        print("Введите корректное значение")

    return True