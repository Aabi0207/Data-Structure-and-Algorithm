# def find_duplicates(list1):
#     duplicate_list = []
#     key_dict = {}
#     for key in list1:
#         if key not in key_dict:
#             key_dict[key] = True
#         elif key not in duplicate_list:
#             duplicate_list.append(key)
#     return duplicate_list
# 
#OR

def find_duplicates(nums):
    nums_dict = {}
    for key in nums:
        nums_dict[key] = nums_dict.get(key, 0) + 1
    key_list = [key for key, count in nums_dict.items() if count > 1]
    return key_list




print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

