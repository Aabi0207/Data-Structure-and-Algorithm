def merge(list1, list2):
    combined_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined_list.append(list1[i])
            i += 1
        else:
            combined_list.append(list2[j])
            j += 1
    while i < len(list1):
        combined_list.append(list1[i])
        i += 1
    while j < len(list2):
        combined_list.append(list2[j])
        j += 1
    return combined_list


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = len(my_list) // 2
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])

    return merge(left, right)

my_list = [3, 1, 4, 2]
print(merge_sort(my_list))