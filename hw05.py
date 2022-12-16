# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = "вап вап кн г кур енш ен ыаап г68 цв к н ш енгр ыаымбфы"
newText = list(filter(lambda i: 'а' not in i and "б" not in i and "в" not in i, text.split()))
print(newText)


# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1,10))

def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)

main(board)


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# пути
pathDecompressed = "C://GitHub//geekbrains//007_python//007_PY_HW05//input.txt"
pathCompressed = "C://GitHub//geekbrains//007_python//007_PY_HW05//output.txt"
pathDecompressedTest = "C://GitHub//geekbrains//007_python//007_PY_HW05//inputtest.txt"

# сжатие
def compress(pathDecompressed, pathCompressed):
    with open(pathDecompressed, "r") as file:
        text = list(file.readline())

        # итоговая строка
        result = ""

        count = 1        
        for i in range(1, len(text)):
            if (text[i - 1] == text[i] and i + 1 < len(text)):
                count = count + 1    
            elif(i + 1 == len(text)):
                count = count + 1    
                result = result + str(count) + text[i - 1]
            else:
                result = result + str(count) + text[i - 1]
                count = 1
        
    # Запись в файл
    with open(pathCompressed, "w") as file:
        file.writelines(result)        


# распаковка
def decompress(pathCompressed, pathDecompressed):    
    with open(pathCompressed, "r") as file:
        text = list(file.readline())

        # итоговая строка
        result = ""      

        for i in range(0, len(text)):
            if(i % 2 == 1):
                result = result + str(int(text[i - 1]) * text[i])
        
    # Запись в файл
    with open(pathDecompressed, "w") as file:
        file.writelines(result)

decompress(pathCompressed, pathDecompressed)