def selection_sort(my_list):
    for i in range(0, len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if not min_index == i:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list

my_list = [5, 6, 7, 3, 2, 9]
print(selection_sort(my_list))
            