salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

money_capital = 0  # подушка безопас.
while months > 0:
    money_capital += salary-spend  # отложенная ЗП в подушку безопасности
    spend += spend * increase  # увеличиваем траты на 3% каждый месяц
    months -= 1  # уменьшаем кол-во месяцев

money_capital = abs(money_capital)
result = round(money_capital, 2)
print(f"Подушка безопасности, чтобы протянуть {10} месяцев без долгов:", result)
