from datetime import datetime
from presentation.handlers.config import today_report, month_report
from shared.utils import get_datetime
from application.report_daily import report_daily

def report_handler(path, data):
    date = get_datetime(datetime.today(), "дата")
    report = input(f"Введите отчет: {today_report}/{month_report}\n")

    if report == today_report:
        report_daily(data, date)
    else:
        print("Введите корректный отчет")