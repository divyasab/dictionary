# Q20.Write a Python program to check a dictionary is empty or not.

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 4Write a Python program to combine two dictionary adding values for common keys. 
# 00, 'b': 400, 'd': 400, 'c': 300})

for i in d1:
    if i in d2:
        d2[i]=d2[i]+d1[i]
    else:
        d2[i]=d1[i]
        print(d2)
