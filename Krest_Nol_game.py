mas_game = [['-1-', '-2-', '-3-'],
            ['-4-', '-5-', '-6-'],
            ['-7-', '-8-', '-9-']]

slov_yach = {1:'00', 2:'01', 3:'02', 4:'10', 5:'11', 6:'12', 7:'20', 8:'21', 9:'22'} #словарь с ячейками
schet = [0, 0, 0] #выигрышей х, у, ничья
def chek_game(l): #проверяем условия завершения игры (есть свободные клетки, нет ли выигрыша х или о.)
    if '-' in l[0][0] or '-' in l[0][1] or '-' in l[0][2] or\
            '-' in l[1][0] or '-' in l[1][1] or '-' in l[1][2] or\
            '-' in l[2][0] or '-' in l[2][1] or '-' in l[2][2]:
        if l[0] == [' X ', ' X ', ' X '] or l[1] == [' X ', ' X ', ' X '] or l[2] == [' X ', ' X ', ' X '] or \
        l[0][0] == ' X ' and l[0][1] == ' X ' and l[0][2] == ' X ' or \
        l[1][0] == ' X ' and l[1][1] == ' X ' and l[1][2] == ' X ' or \
        l[2][0] == ' X ' and l[2][1] == ' X ' and l[2][2] == ' X ' or \
        l[0][0] == ' X ' and l[1][1] == ' X ' and l[2][2] == ' X ' or \
        l[2][0] == ' X ' and l[1][1] == ' X ' and l[0][2] == ' X ':
            print('Игра закончена. Выиграл х!!!')
            schet[0] += 1
            return False
        elif l[0] == [' O ', ' O ', ' O '] or l[1] == [' O ', ' O ', ' O '] or l[2] == [' O ', ' O ', ' O '] or \
        l[0][0] == ' O ' and l[0][1] == ' O ' and l[0][2] == ' O ' or \
        l[1][0] == ' O ' and l[1][1] == ' O ' and l[1][2] == ' O ' or \
        l[2][0] == ' O ' and l[2][1] == ' O ' and l[2][2] == ' O ' or \
        l[0][0] == ' O ' and l[1][1] == ' O ' and l[2][2] == ' O ' or \
        l[2][0] == ' O ' and l[1][1] == ' O ' and l[0][2] == ' O ':
            print('Игра закончена. Выиграл o!!!')
            schet[1] += 1
            return False
        return True
    print('Ходы закончились. Ничья!')
    schet[2] += 1
    return False

def vivod_mas(mas): #Выводим поле игры
    print(f'''_____________
|{mas[0][0]}|{mas[0][1]}|{mas[0][2]}|
_____________
|{mas[1][0]}|{mas[1][1]}|{mas[1][2]}|
_____________
|{mas[2][0]}|{mas[2][1]}|{mas[2][2]}|
_____________
''')

def vibor(t): #Выбор ячейки для хода
    a = input(f"Введите номер клетки для {t}: ")
    while True:
        if a.isdigit() and 0 < int(a) < 10:
            if mas_game[int(slov_yach[int(a)][0])][int(slov_yach[int(a)][1])] != ' X ' \
                    and mas_game[int(slov_yach[int(a)][0])][int(slov_yach[int(a)][1])] != ' O ':
                return int(a)
            else:
                a = input(f"ячейка занята. Введите число СВОБОДНОЙ ячейки для {t}:")
        else:
            a = input(f"ввод некорректный. Введите ЧИСЛО свободной ячейки для {t}:")

def hod(t): #ход х или о
    tmp = vibor(t)
    mas_game[int(slov_yach[tmp][0])][int(slov_yach[tmp][1])] = ' X ' if t == 'x' else ' O '
    vivod_mas(mas_game)

tmp = input('Для начала игры нажмите "Enter". Для выхода введите "n" или "N"')

while tmp != 'n' and tmp != 'N': #цикл до тех пор, пока мы в начале игры выбираем что-либо, кроме nN
    mas_game = [['-1-', '-2-', '-3-'], #обнуляем массив перед началом игры
                ['-4-', '-5-', '-6-'],
                ['-7-', '-8-', '-9-']]
    vivod_mas(mas_game) # выводим первоначальный массив
    hod('x')
    hod('o')
    while True: # бесконечный цикл пока игра не закончится (при выигрыше или ничьей)
        if chek_game(mas_game):
            hod('x')
        else:
            break
        if chek_game(mas_game):
            hod('o')
        else:
            break
    tmp = input('Для начала новой игры нажмите "Enter". Для выхода введите "n" или "N"')
print(f"Всего сыграно {sum(schet)} игр: 'Х' выиграл - {schet[0]}; 'O' выиграл - {schet[1]}; ничья - {schet[2]} .") #Вывод статистики игр