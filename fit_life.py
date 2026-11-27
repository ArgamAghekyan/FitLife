WATER_PER_KG = 30  # мл воды на 1 кг веса
ML_IN_LITER = 1000  # мл в 1 литре


user_name = input('Как вас зовут?: ').capitalize()
print(f'Здравствуйте, {user_name}!')


while True:
    try:
        user_age = int(input('Сколько вам лет?: '))
        break
    except ValueError:
        print('Нужно ввести целое число')


while True:
    try:
        user_weight = float(input('Какой ваш вес(в кг, пример: 62.0)?: '))
        break
    except ValueError:
        print('Нужно ввести число с точкой')


while True:
    try:
        user_height = float(input('Какой ваш рост(в метрах, пример: 1.79)?: '))
        break
    except ValueError:
        print('Нужно ввести число с точкой')


# расчёт индекса массы тела
bmi = user_weight / user_height**2
# расчёт нормы воды и перевод в литры
water_l = user_weight * WATER_PER_KG / ML_IN_LITER

print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {bmi:.1f}')
print(f'Рекомендуемая норма воды: {water_l:.1f} л. в день')
print()
print('Расчет окончен. Будьте здоровы!')
