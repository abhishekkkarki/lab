#check whether a passed string is palindrome or not
def palindromeCheck(word):
    word=word.upper()
    rev=word[::-1]
    if rev==word:
        print("It is a Palindrome")
    else:
        print("It is not a Palindrome")
        
palindromeCheck("Alila")