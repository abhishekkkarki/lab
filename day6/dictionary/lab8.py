#merge two Python dictionaries
dict={}
dict1={1:"b",2:"a",3:"d"}
dict2={"x":"d","y":"a","z":"y"}
dict=dict1.copy()
dict.update(dict2)
print(dict)
