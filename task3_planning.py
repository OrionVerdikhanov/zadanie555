from datetime import datetime, timedelta

def future_date(days_from_now):
    """
    Возвращает дату, которая наступит через указанное
    количество дней от текущей даты в формате YYYY-MM-DD.

    :param days_from_now: Количество дней от текущей даты (int).
    :return: Строка с отформатированной будущей датой 'YYYY-MM-DD'.

    Примеры:
    >>> future_date(30)
    '2024-09-08'
    >>> future_date(-10)
    '2024-07-30'
    """
    # Получение текущей даты и времени
    today = datetime.now()

    # Вычисление даты через указанное количество дней
    result_date = today + timedelta(days=days_from_now)

    # Форматирование будущей даты в строку в формате YYYY-MM-DD
    formatted_future_date = result_date.strftime('%Y-%m-%d')
    return formatted_future_date

if __name__ == '__main__':
    days = 30  # Пример: 30 дней от текущей даты
    print(f'Date {days} days from now: {future_date(days)}')
