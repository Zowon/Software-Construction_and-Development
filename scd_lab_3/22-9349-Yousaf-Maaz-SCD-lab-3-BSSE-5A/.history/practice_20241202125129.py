# def isplaindrome(word)->bool:
#     if len(word) == 1:
#         return  True
#     if word[0] != word[-1]:
#         return False
#     return isplaindrome(word[1:-1])

# print (isplaindrome("racecar"))   


a = '5'

if not isinstance(a, int):
    raise TypeError("a must be an integer")