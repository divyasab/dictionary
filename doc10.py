# Q10.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. 
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
a=int(input("enter the number"))
b={}
for a in range(1,a+1):
    b.update({a:a**2})
print(b)

