from infrastracture.storage import save_data
from shared.utils import get_datetime

def add_transaction(path, date, type_op, amount, category, description, data):
    date = get_datetime(date)

    if type_op not in ("доход", "расход"):
        return False, "Некорректная тип операции"

    try:
        amount = int(amount)
    except ValueError:
        return False, "Сумма должна быть числом"

    if amount <= 0 :
        return False, "Сумма должна быть больше 0"

    if not category.strip():
        return False, "Категория не может быть пустой"

    if not description.strip():
        return False, "Описание не может быть пустым"

    operation = {"type": type_op,
                 "date": date,
                 "amount": amount,
                 "category": category,
                 "description": description}

    data.append(operation)
    save_data(path, data)

    return True, None