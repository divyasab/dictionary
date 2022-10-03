# Write a program to print the top 3 highest keys of a given dictionary.

my_dict = {
'a':50, 
'b':58,
'c': 56,
'd':40,
'e':100, 
'f':20
}
x=list(my_dict.keys())
d=dict()
x.sorted()
x=x[1:3]
print(x)

