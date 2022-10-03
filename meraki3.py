# Write a program to print 'exists' if entered key already exists in the 
# dictionary and print 'not exists' if the entered key does not exist.

# program :-

# Code Example
# dict1={“name”:”Raju”, “marks”:56}

# Output :-
# enter the value=name Raju

# a={"chitra":"name","sable":"rupa"}

dict1={"name":"Raju","marks":56}
a=input("enter the value=")
if (a=="name"):
  print (dict1["name"])
elif(a=="marks"):
  print(dict1["marks"])
else:
  print ("invalid input")


