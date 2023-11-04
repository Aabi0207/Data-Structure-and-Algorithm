# def group_anagrams(words):
#     anagram_list = []
#     used_index = []
#     for word in words:
#         if words.index(word) not in used_index:
#             same_letter_list = []
#             same_letter_list.append(word)
#             for i in range(words.index(word) + 1, len(words)):
#                 result = all(char in words[i] for char in word)
#                 if result and i not in used_index:
#                     used_index.append(i)
#                     same_letter_list.append(words[i])
#             anagram_list.append(same_letter_list)
#     return anagram_list
# 
#OR

def group_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        canonical = ''.join(sorted(string))
        if canonical in anagram_groups:
            anagram_groups[canonical].append(string)
        else:
            anagram_groups[canonical] = [string]
    return list(anagram_groups.values())




print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""