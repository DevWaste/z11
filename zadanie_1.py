my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def recursive(index = 0):
    if len(my_list) == index:
        print("Конец списка")
        return
    print(my_list[index])
    recursive(index+1)

recursive()    