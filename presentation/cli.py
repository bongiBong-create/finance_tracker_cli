from presentation.config  import cmd_add, cmd_balance, cmd_out, cmd_remove, cmd_transactions
from infrastracture.storage import init_path
from infrastracture.storage import init_storage
from infrastracture.storage import get_data
from presentation.handlers.add_handler import add_handler
from presentation.handlers.remove_handler import remove_handler
from presentation.handlers.balance_handler import balance_handler
from presentation.handlers.transactions_handler import transactions_handler
from presentation.handlers.out_handler import out_handler

def start_cli():
    print("Добрый день!")
    path = init_path()
    init_storage(path)

    commands = {
        cmd_add: add_handler,
        cmd_remove: remove_handler,
        cmd_balance: balance_handler,
        cmd_transactions: transactions_handler,
        cmd_out: out_handler,
    }

    flag = True

    while flag:
        data = get_data(path)
        command = input(f"Введите команду: {"/".join(commands.keys())}\n").lower()
        handler = commands.get(command)

        if handler:
            flag = handler(path, data)
        else:
            print("Введите корректную команду")