def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    midpoint = len(aStr) // 2

    if len(aStr) == 0:
        return False
    elif char == aStr[midpoint]:
        return True
    elif char > aStr[midpoint]:
        return isIn(char, aStr[midpoint+1:])
    else:
        return isIn(char, aStr[:midpoint])
    
print(isIn('i', 'abcdefghijklmnopqrstuvwxyz'))