import json
import subprocess as sp
import time
from random import randint


def map_checking_neighbours(map, line, col):
    neighbours = [(line + a[0], col + a[1]) for a in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                  if (0 <= line + a[0] <= len(map) - 1) and (0 <= col + a[1] <= len(map) - 1)]
    if (neighbours[0] == -1 and neighbours[1] == -1 and neighbours[2] == -1 and neighbours[3] == -1):
        return False
    return True

def map_checking_borders(map):
    for i in range(len(map) - 1):
        if map[0][i] == -1 or map[len(map)-1][i] == -1\
                or map[i][0] == -1 or map[i][len(map)-1] ==-1:
            return False
    return True

def map_checking_move(map, line, col):
    if (line<0 and line > len(map) - 1 and col < 0 and col > len(map)):
        return False
    return True

def map_checking_first_move(map, line, col):
    n = len(map)//2
    if line>=n-1 and line<= n+3 and col >=n-1 and col <=n+3:
        return True
    return False

def map_generation():
    a = 11
    arr = [[randint(0, 9) for j in range(a)] for i in range(a)]
    return (len(arr), arr)

def making_map(map):
    string = ""
    for elem in map:
        a = " ".join(map(str, elem))
        string+= a + '\n'
    return string

def print_winner(player1, player2):
    if (player1 > player2):
        print(f'Игрок1 победил, игровой счет: {player1};{player2}')
    else:
        print(f'Игрок2 победил, игровой счет: {player2};{player1}')

    for row in my_list[0]["map"]:
        print(*row)

my_list = [
        {
            "m": map_generation()[0],
            "map": map_generation()[1],
            "line": -1,
            "column": -1,
        }
]

def algorithms_test():
    player1 = 0
    player2 = 0
    commands = ["command1", "command2"]
    proc1 = sp.Popen(commands[0],shell=True,stdin=sp.PIPE, stdout=sp.PIPE)
    proc2 = sp.Popen(commands[0],shell=True,stdin=sp.PIPE, stdout=sp.PIPE)

    proc1.stdin.writelines(str(my_list[0]["m"]) + "\n" + making_map(my_list[0]["map"]) + "\n"
                           + str(my_list[0]["line"]) + " " + str(my_list[0]["column"]))
    out1 = proc1.stdout.readline().rsplit()[0].decode()
    line1 = out1[0]
    col1 = out1[1]
    if map_checking_first_move(my_list[0]["map"],line1,col1):
        player1 += my_list[0]["map"][int(line1)][int(col1)]
        my_list[0]["map"][int(line1)][int(col1)] = -1
        my_list[0]["line"] = int(line1)
        my_list[0]["column"] = int(col1)


    proc2.stdin.writelines(str(my_list[0]["m"]) + "\n" + making_map(my_list[0]["map"]) + "\n"
                          + str(my_list[0]["line"]) + " " + str(my_list[0]["column"]))
    out2 = proc2.stdout.readline().rsplit()[0].decode()
    line2 = out2[0]
    col2 = out2[1]
    if map_checking_move(my_list[0]["map"],line2, col2):
        player2 += my_list[0]["map"][int(line2)][int(col2)]
        my_list[0]["map"][int(line1)][int(col2)] = -1
        my_list[0]["line"] = int(line2)
        my_list[0]["column"] = int(col2)

    while map_checking_borders(my_list[0]["map"]) and map_checking_neighbours(my_list[0]["map"],my_list[0]["line"],
                                                                              my_list[0]["column"]):
        proc1.stdin.writelines(str(my_list[0]["line"]) + " " + str(my_list[0]["column"]))
        out1 = proc1.stdout.readline().rsplit()[0].decode()
        line1 = out1[0]
        col1 = out1[1]
        if map_checking_move(my_list[0]["map"],line1, col1):
            player1 += my_list[0]["map"][int(line1)][int(col1)]
            my_list[0]["map"][int(line1)][int(col1)] = -1
            my_list[0]["line"] = int(line1)
            my_list[0]["column"] = int(col1)
        if map_checking_neighbours(my_list[0]["map"],my_list[0]["line"],my_list[0]["column"]):
            proc2.stdin.writelines(str(my_list[0]["line"]) + " " + str(my_list[0]["column"]))
            line2 = out2[0]
            col2 = out2[1]
            if map_checking_move(my_list[0]["map"], line2, col2):
                player2 += my_list[0]["map"][int(line2)][int(col2)]
                my_list[0]["map"][int(line2)][int(col2)] = -1
                my_list[0]["line"] = int(line2)
                my_list[0]["column"] = int(col2)
            else:
                print_winner(player1, player2)
        else:
            print_winner(player1, player2)
    print_winner(player1, player2)
    proc1.kill()
    proc2.kill()

if __name__ == '__main__':
    algorithms_test()