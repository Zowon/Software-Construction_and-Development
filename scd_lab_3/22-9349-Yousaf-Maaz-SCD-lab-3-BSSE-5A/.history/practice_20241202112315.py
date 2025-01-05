def isplaindrome(word)->bool:
    if len(word) == 1:
        return  True
    if word[0] != word[-1]:
        return False
    isplaindrome(word[1:-1])
   