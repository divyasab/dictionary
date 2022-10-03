# Count the total number of items from the values of the dictionary which are in 
# the form of a list.

dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
sum=0
for i in dict1.values():
  for item in i:
    sum+=1
print(sum)

