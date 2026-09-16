
# Константы для расчётов
WATER_PER_KG = 30
ML_IN_LITER = 1000


print("Добро пожаловать в Fit Life!")
print()


user_name = input("Привет! Введи своё имя: ").title()
while True:
    try:
        user_age = int(input("Введи свой возраст: "))
        if user_age <= 0:
            print("Возраст должен быть больше 0")
            continue
        break
    except ValueError:
        print("Можно вводить только цифры!")


while True:
    try:
        user_weight = float(input("Введи свой вес (В кг): ").replace(',', '.'))
        if user_weight <= 0:
            print("Вес должен быть больше 0")
            continue
        break
    except ValueError:
        print("Можно вводить только цифры!")


while True:
    try:
        user_height = float(input("Введи свой рост(В метрах): ")
                            .replace(',', '.'))
        if user_height <= 0:
            print("Рост должен быть больше 0")
            continue
        break
    except ValueError:
        print("Можно вводить только цифры!")
# Рассчёт ИМТ
bmi = round(user_weight / (user_height ** 2), 1)

# Расчёт нормы воды
water_l = round((user_weight * WATER_PER_KG) / ML_IN_LITER, 2)


print(f"""Отчет для пользователя: {user_name} ({user_age} г).
Твой Индекс Массы Тела: {bmi}
Рекомендуемая норма воды {water_l} л. в день

Расчет окончен. Будьте здоровы! """)
