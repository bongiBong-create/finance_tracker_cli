from infrastracture.storage import save_data
from shared.utils import check_index

def remove_transaction(path, index, data):
    if check_index(index, data):
        data.pop(index)
        save_data(path, data)
        return True

    return False