import sys
import time


def run():
    is_first_step = False
    is_second_player = False
    rows = int(sys.stdin.readline()) #размерность поля
    map = []
    for x in range(rows): #заполняем поле значениями с консоли
        line = sys.stdin.readline()
        map.append([int(y) for y in line.split()])
    coord = sys.stdin.readline().split(" ")
    cell = (int(coord[0]), int(coord[1]))
    map[cell[0]][cell[1]] = -1
    if cell[0] == cell[1] == -1:
        opt = -1
        differences = []
        for i in range(int((rows - 1) / 2 - 1), int((rows - 1) / 2 + 2)):
            for j in range(int((rows - 1) / 2 - 1), int((rows - 1) / 2 + 2)):
                if rows > 3:
                    opt = map[i][j]
                    next_el = max(map[i + 1][j], map[i - 1][j], map[i][j + 1], map[i][j - 1])
                    differences.append((opt - next_el, (i, j)))
                elif map[i][j] > opt:
                    opt = map[i][j]
                    opt_coord = (i, j)
        if rows > 3:
            result = max(differences)[1]
            map[result[0]][result[1]] = -1
            sys.stdout.write(str(result[0]) + " " + str(result[1]) + "\n")
        else:
            map[opt_coord[0]][opt_coord[1]] = -1
            sys.stdout.write(str(opt_coord[0]) + " " + str(opt_coord[1]) + "\n")
    else:
        is_second_player = True
        is_first_step = True
    while True:
        if is_first_step:
            if not is_second_player:
                new_cell = sys.stdin.readline().split(" ")
                map[int(new_cell[0])][int(new_cell[1])] = -1
                cell = (int(new_cell[0]), int(new_cell[1]))
            x = cell[0]
            y = cell[1]
            if not check_condition(x, y, rows):
                return "Вышли за границу\n"
            # tuples со значениями соседей и их координатами
            left = (map[x][y - 1], (x, y - 1)) if check_condition(x, y - 1, rows) else -1
            right = (map[x][y + 1], (x, y + 1)) if check_condition(x, y + 1, rows) else -1
            top = (map[x - 1][y], (x - 1, y)) if check_condition(x - 1, y, rows) else -1
            bottom = (map[x + 1][y], (x + 1, y)) if check_condition(x + 1, y, rows) else -1
            if left == right == top == bottom == -1:
                sys.stdout.write("Нельзя сделать следующий ход\n")
            differences = []
            for i in [left, right, top, bottom]:
                if i == -1 or i[0] == -1:
                    continue
                x1 = i[1][0]
                y1 = i[1][1]
                opt = map[x1][y1] #значение соседней клетки
                #проверяем соседей на шаг вперед
                new_left = check_y(cell, map, x1, y1 - 1, y1 - 1 < 0)
                new_right = check_y(cell, map, x1, y1 + 1, y1 + 1 > rows - 1)
                new_top = check_x(cell, map, x1 - 1, y1, x1 - 1 < 0)
                new_bottom = check_x(cell, map, x1 + 1, y1, x1 + 1 > rows - 1)
                # максимальное значение из всех соседей opt
                next_el = max(new_left, new_right, new_top, new_bottom)
                differences.append((opt - next_el, (x1, y1))) #массив разниц
            if len(differences) != 0:
                result = max(differences)[1] #берем клетку с максимальной разницей
                map[result[0]][result[1]] = -1
                time.sleep(1)
                sys.stdout.write(str(result[0]) + " " + str(result[1]) + "\n")
            else:
                sys.stdout.write("Невозможно сделать ход\n")
        is_first_step = True
        is_second_player = False


def check_condition(x, y, rows):
    return 0 <= x <= rows - 1 and 0 <= y <= rows - 1


def check_x(cell, map, x1, y1, condition):
    if condition:
        element = -1
    elif (x1, y1) != cell:
        element = map[x1][y1]
    else:
        element = -1
    return element


def check_y(cell, map, x1, y1, condition):
    if condition:
        element = -1
    elif (x1, y1) != cell:
        element = map[x1][y1]
    else:
        element = -1
    return element


if __name__ == '__main__':
    run()