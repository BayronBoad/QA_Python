#rating >=7
#min_balance = 5000

user_raiting = int(input('Ваш кредитный рейтинг: '))
Balance = int(input('Ваш доход: '))

if user_raiting >= 7: 
    print("У вас хороший кредитный рейниг")
    if Balance >=5000:
        print("Вам одобрен кредит")
    elif balance <5000: 
        print("Ваш доход ниже 5000 фантиков, cтарайся лучше")
else:
    print("Больше не бери займов, иди домой")
