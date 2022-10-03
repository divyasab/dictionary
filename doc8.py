# Write a Python program to check whether a given key already exists in a dictionary.
a={10:1,16:2,89:23,5:76,9:10}
b={}
for i in a:
    if a in b:
        print("keys is present in dictionary")
    else:
        print("keys not present in dictionary")

