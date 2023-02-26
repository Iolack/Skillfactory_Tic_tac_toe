print("Привет. Это игра крестики-нолики.")

def dyrak ():
    global gamer1, gamer2
    gamer2 = '1'
    gamer1 = input()
    while True:
        if gamer1 in 'x':
            gamer2 = 'o'
            return gamer2
            break
        # rus
        elif gamer1 in 'х':
            gamer2 = 'о'
            return gamer2
            break
        elif gamer1 in 'о':
            gamer2 = 'х'
            return gamer2
            break
        elif gamer1 in 'o':
            gamer2 = 'x'
            return gamer2
            break
        else:
            print('Введите правильный символ')
            gamer1 = input()
            continue

tic_tac = list(range(1, 10))
def board(tic_tac):
    print("-" * 13)
    for i in range(3):
        print("|", tic_tac[0+i*3], "|", tic_tac[1+i*3],"|", tic_tac[2+i*3])
        print("-" * 13)

def place_symbol_g1():
    flag = False
    while not flag:
        place = input('Введите местоположение символа первого игрока ')
        try:
            place = int(place)
        except:
            print("Неправильное значение, введите число.")
            continue
        if 1 <= place <= 9:
            if (str(tic_tac[place - 1]) not in gamer1) and (str(tic_tac[place - 1]) not in gamer2):
                tic_tac[place - 1] = gamer1
                board(tic_tac)
                flag = True
            else:
                print("Место занято")
        else:
            print("Такого местоположения нет")
            continue

def place_symbol_g2():
    flag = False
    while not flag:
        place = input('Введите местоположение символа второго игрока ')
        try:
            place = int(place)
        except:
            print("Неправильное значение, введите число.")
            continue
        if 1 <= place <= 9:
            if (str(tic_tac[place-1]) not in gamer1) and (str(tic_tac[place-1]) not in gamer2):
                tic_tac[place - 1] = gamer2
                board(tic_tac)
                flag = True
            else:
                print("Место занято")
        else:
            print("Такого местоположения нет")
            continue

def check_win(tic_tac):
    win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_comb:
        if tic_tac[i[0]] == tic_tac[i[1]] == tic_tac[i[2]]:
            return tic_tac[i[0]]
    return False

def main(tic_tac):
    print("Выберите символ первого игрока х или о ")
    dyrak()
    board(tic_tac)
    count = 0
    while True:
        place_symbol_g1()
        if check_win(tic_tac):
            print("Победил игрок игравший за", gamer1)
            break
        else:
            count += 1
        if count == 9:
            print("Ничья!")
            break
        place_symbol_g2()
        if check_win(tic_tac):
            print("Победил игрок игравший за", gamer2)
            break
        else:
            count += 1

main(tic_tac)
while True:
    print("Ещё партейку? Введите Да или Нет")
    answer = input()
    if "Да" in answer:
        tic_tac = list(range(1, 10))
        main(tic_tac)
    elif "Нет" in answer:
        print("Пока!")
        break
    else:
        print("Не понятное значение")






