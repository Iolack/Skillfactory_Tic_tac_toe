print("Привет. Это игра крестики-нолики.")
print("Выберите символ первого игрока х или о")

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





dyrak()

print('Введите координаты символа первого игрока')

tic_tac = ([' ', '1', '2', '3'], [1, '-', '-', '-'], [2, '-', '-', '-'], [3, '-', '-', '-'])
for i in tic_tac:
    print(*i)