from shared.utils import check_length

def get_balance(path, data):
    if check_length(data):
        incomes = [el["amount"] for el in data if el["type"]== "доход"]
        expenditures = [el["amount"] for el in data if el["type"]== "расход"]
        return sum(incomes) - sum(expenditures)

    return 0