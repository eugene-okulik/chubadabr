from random import randrange, random
salary = int(input("What's your salary? "))
bonus = bool(randrange(0, 2))
if bonus:
    print(f"{salary}, {bonus} - '${int(salary / random())}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
