from infrastracture.storage import get_data
from shared.utils import filtered_transactions, check_length

def get_transactions(path, data, category, categories):

    if check_length(data):
        if category == "общие":
            return data, None
        elif category in categories:
            return filtered_transactions(data, category), None
        else:
            return False, "Категории не существует"
    else:
        return False, "Транзакции отсутствуют"
