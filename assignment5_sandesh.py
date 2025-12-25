def recurisve_palindrome(word):
    if len(word) <= 1:
        return True
    
    if word[0] != word[-1]:
        return False
    
    return recurisve_palindrome(word[1:-1])

