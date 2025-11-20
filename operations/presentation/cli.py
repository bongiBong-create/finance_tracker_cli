operations = []

def start_cli():
    while True:
        command = input("Введите команду: Добавить/Удалить/Баланс/Операции/Выход\n").lower()

        match command:
            case "добавить":
                type_operation = input("Введите тип операции: Доход/Расход\n").strip().lower()
                if type_operation == "доход" or type_operation == "расход":
                    amount = int(input("Введите сумму\n"))
                    description = input("Введите на что потратили\n")
                    operation = {"type": type_operation, "amount": amount, "description": description}
                    operations.append(operation)
                    print("Операция успешно добавлена")
                else:
                    print("Введите корректную операцию")
            case "удалить":
                index = int(input("Введите номер операции\n"))
                operations.pop(index - 1)
                print("Операция успешно удалена")
            case "баланс":
                incomes = [el["amount"] for el in [*filter(lambda x: x["type"] == "доход", operations)]]
                expenditures = [el["amount"] for el in [*filter(lambda x: x["type"] == "расход", operations)]]
                print(sum(incomes) - sum(expenditures))
            case "операции":
                if len(operations) > 0:
                    for i, value in enumerate(operations):
                        print(f"Задач №{i + 1}\n"
                              f"Тип: {value['type']}\n"
                              f"Описание: {value['description']}")
                else:
                    print("Нет операций")
            case "выход":
                break
            case _:
                print("Введите корректную команду")

start_cli()