def first_non_repeating_char(string):
    str_dict = {char: string.count(char) for char in string}
    for char in string:
        if str_dict[char] == 1:
            return char



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""