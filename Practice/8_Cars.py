#создаём список автомобилей
cars = [] 

#Данные пользователя
num_cars = int(input("Введите количество автомобилей для оценки: "))
for i in range(num_cars):
    brand = input("Введите марку автомобиля: ")
    year = int(input("Введите год выпуска автомобиля: "))
    mileage = float(input("Введите пробег автомобиля (в км): "))
    condition = input("Введите состояние автомобиля (новый/бу): ")

    # Оценка стоимости автомобиля
    base_price = 20000
    brand = 1 if condition == 'BMW' else 0.5 
    year_f= 0.95 if condition == 'новый' else 0.85  # Новый автомобиль дороже
   
    # Оценка даты выпуска
    if year <= 2000:
        year_f = 0.25
    elif year == 2015:
        year_f = 0.5
    elif year >= 2020:
        year_f = 1        
    else:
        year_f = 0.1

    # Оценка пробега
    if mileage <= 100000:
        mileage_f = 1
    else:
        mileage_f = 0.5
    price = brand * base_price * year_f* mileage_f

    # Вывод оценки стоимости автомобиля
    print(f"Оценка стоимости автомобиля марки {brand}, год выпуска {year}, пробег {mileage} км, состояние автомобиля -  {condition}: {price:.2f} руб.")