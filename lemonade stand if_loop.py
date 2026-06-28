stand_money = [200, 300, 55, 27, 11, 5]



for money in stand_money:
    if money > 200:
        print("you have a very successful day!")
    elif money > 100:
        print("you had a good day!")
    elif money > 50:
        print("you had a decent day.")
    elif money > 25:
        print("you had a rough day.")
    elif money > 10:
        print("you had a terrible day.")
    else:
        print("you had a very bad day.")

