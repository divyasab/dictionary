# Write a Python program to map two lists into a dictionary.

a=["divya","sable","mummy","varsha"]
b=[12,23,45,78,]
n={}
for i in range (len(b)):
    n.update({a[i]:b[i]})
print(n)

