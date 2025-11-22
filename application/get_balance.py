from infrastracture.storage import get_data
from shared.utils import check_length

def get_balance(path):
    transactions = get_data(path)

    if check_length(transactions):
        incomes = [el["amount"] for el in [*filter(lambda x: x["type"] == "доход", transactions)]]
        expenditures = [el["amount"] for el in [*filter(lambda x: x["type"] == "расход", transactions)]]
        return sum(incomes) - sum(expenditures)
    else:
        return 0