def num_guesser():
    print('Угадай, какое число загадано')
    num = 777
    while True:
        guess = int(input("Введите число "))
        if guess == num:
            print("Поздравляю! Вы угадали!")
            break
        else:
            print("попробуйте снова")


num_guesser()
