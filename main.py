import random

def roll_dice():
    """Бросок костей"""
    return random.randint(1, 6)

def main():
    print("Добро пожаловать в игру в кости!")

    player_score = 0
    computer_score = 0

    while True:
        input("Нажмите Enter, чтобы бросить кости...")
        player_roll = roll_dice()
        computer_roll = roll_dice()

        print(f"Вы бросили: {player_roll}")
        print(f"Компьютер бросил: {computer_roll}")

        if player_roll > computer_roll:
            print("Вы победили в этом раунде!")
            player_score += 1
        elif player_roll < computer_roll:
            print("Вы проиграли в этом раунде!")
            computer_score += 1
        else:
            print("Ничья в этом раунде!")

        print(f"Ваш счет: {player_score}, Счет компьютера: {computer_score}")

        if input("Хотите сыграть еще раз? (да/нет): ").lower() != "да":
            break

    print("Спасибо за игру!")

if name == "main":
    main()
