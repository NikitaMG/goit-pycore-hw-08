import datetime


def get_days_from_today(date):
    try:
        user_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        current = datetime.date.today()
        delta = current - user_date
        return delta.days
    except ValueError:
        return "Формат дати введено неправильно! Правильний формат: 'РРРР-ММ-ДД'. "


customer_date = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
print(get_days_from_today(customer_date))






