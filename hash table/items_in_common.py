def items_in_common(list1, list2):
    keys_dict = {key: True for key in list1}
    for key in list2:
        if key in keys_dict:
            return True
    return False

list1 = [1, 3, 5]
list2 = [2, 6, 9]

print(items_in_common(list1, list2))