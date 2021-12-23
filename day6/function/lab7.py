#function that accepts a string and calculate the number of upper case letters and lower case letters
def caseCheck(word):
    u,l=0,0
    for i in word:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
    print(f"{word} has {u} Upper case and {l} Lower case letters")
            
caseCheck("AdgTaf")