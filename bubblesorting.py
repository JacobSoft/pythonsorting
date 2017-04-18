def bubbleSort(some_list):
    for x in range(0, len(some_list) -1):
        for y in range(0, len(some_list) -1 -x):
            if some_list[y] > some_list[y+1]:
                some_list[y], some_list[y+1] = some_list[y+1], some_list[y]
    return some_list

my_list=[67, 45, 2, 13, 1, 998]
print(bubbleSort(my_list))

