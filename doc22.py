# Q22. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
a={'1':['a','b'], '2':['c','d']}
for i in a["1"]:
    for j in a["2"]:
        n=i+j
        print(n)


# print(m)

# 


# a="divya"
# b="23.6"
# c=13
# d="manisha"
# print()

# o/p divyamanisha33 

# a="divya"
# b="sable"
# print(a,"\t",b)


a="navgurukul is the small indin"
print("nav\tguru\nkul is\t the \tsmall\n india")