# Write a program such that the below given dictionaries are into a single 
# dictionary and add the values having same key.

# program :-

# Code Example
# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}

# # Output :-
# {1: 10, 2: 60, 3: 30, 5: 50, 6: 60}
# dic1={1:10, 2:20}
# dic2={3:30,2:40}                                        
# dic3={5:50,6:60}
# for i in dic2:
#     if i in dic1:
#         dic2[i]=dic2[i]+dic1[i]
#         print(dic2[i])
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)



a={1:10,2:20}
b={3:30,2:40}
c={5:50,6:60}
for i in b:
    if i in a:
        b[i]=b[i]+a[i]
        print(b[i])
a.update(b)
a.update(c)
print(a)
