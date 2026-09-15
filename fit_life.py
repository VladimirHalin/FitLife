#Константы
WATER_PER_KG = 30
ML_IN_LITTER = 1000


print("Добро пожаловать в Fit Life!")
print()


#Данные пользователя
user_name = input("Привет! Введи своё имя: " ).title()
#Проверка, вводит ли человек цифры или буквы
while True:
    try:
        user_age = int(input("Введи свой возраст: "))
        user_weight = float(input("Введи свой вес (В кг): ").replace(',','.'))
        user_height = float(input("Введи свой рост(В метрах): ").replace(',','.'))
        break
    except ValueError:
        print("Можно вводить только цифры!")


#Рассчёт Индекса Массы Тела
bmi = round(user_weight / (user_height ** 2), 1)


#Рассчёт нормы воды
water_ml = user_weight * WATER_PER_KG
water_l = round(water_ml / ML_IN_LITTER, 2 )


#Вывод данных
print(f"""Отчет для пользователя: {user_name} ({user_age} г). 
Твой Индекс Массы Тела: {bmi}
Рекомендуемая норма воды {water_l} л. в день

Расчет окончен. Будьте здоровы! """)
