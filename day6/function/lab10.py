# Accept string from the user and display only those characters which are present at an even index
def evenIndex(word):
    l=len(word)
    for i in range(0,l,2):
        print(word[i])
evenIndex("introduction")