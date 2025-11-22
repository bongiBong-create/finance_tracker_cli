from infrastracture.storage import save_data

def remove_transaction(path, index, data):
    if 0 <= index < len(data):
        data.pop(index)
        save_data(path, data)
        return True

    return False