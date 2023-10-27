import pandas as pd

# Завантажимо дані з 27.09.2023 по 27.09.2023
# Довелось вводити в ручну
data = pd.read_csv('data.csv')

# Реалізація стратегії торгівлі
def trading_strategy(data):
    capital = 1000000  # Початковий капітал (нехай буде 1 мільйон доларів)
    parts = 15  # Кількість частин, на які ділимо капітал

    # Розподілимяємо капітал на частини
    capital_per_part = capital / parts

    # Ініціалізуємо змінні для підрахунку статистики
    profitable_trades = 0
    losing_trades = 0
    total_profit_percentage = 0

    for index, row in data.iterrows():
        buy_price = row['Buy Price']
        sell_price = buy_price * 1.04  # Ордер на продаж прибуткової позиції

        for i in range(parts):
            # Розміщуємо ордери на купівлю
            entry_price = buy_price * (1 + (i+1) * 0.02)
            position_size = capital_per_part / entry_price

            # Перевіряємо, чи досягнуті умови продажу
            if entry_price >= sell_price:
                profitable_trades += 1
                total_profit_percentage += (sell_price / buy_price - 1) * 100
            else:
                losing_trades += 1

    # Виводимо статистику
    print(f'Кількість прибуткових угод: {profitable_trades}')
    print(f'Кількість збиткових угод: {losing_trades}')
    print(f'Загальний прибуток у відсотках: {total_profit_percentage:.2f}%')

trading_strategy(data)
