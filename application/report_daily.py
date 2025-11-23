from shared.utils import print_transactions

def report_daily(data, date):
    data = [el for el in data if el["date"].split()[0] == date]

    print_transactions(data)
    print(f"Кол-во транзакций: {len(data)}")
