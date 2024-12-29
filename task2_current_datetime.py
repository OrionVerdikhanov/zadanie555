from datetime import datetime

def display_current_datetime():
    """
    Выводит текущее время и дату в формате YYYY-MM-DD HH:MM:SS,
    день недели и номер недели в году.
    """
    # Получение текущего времени и даты
    now = datetime.now()

    # Форматирование даты и времени
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

    # Получение дня недели (полное название) и номера недели
    day_of_week = now.strftime('%A')
    week_number = now.isocalendar()[1]

    print(f'Current date and time: {formatted_date}')
    print(f'Day of the week: {day_of_week}')
    print(f'Week number: {week_number}')

if __name__ == '__main__':
    display_current_datetime()
