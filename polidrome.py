def ifPalindrome(string):
    if string == "":  # BASE CASE CONDITION
        return True
    elif len(string) == 1:  # BASE CASE CONDITION
        return True
    elif string[0] == string[len(string)-1]:  # RECURSION
        return ifPalindrome(string[1:][:-1])
    else:
        return False
str1=input('enter string:')
print(ifPalindrome(str1))