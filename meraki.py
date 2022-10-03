# Create a dictionary from 2 lists, where the elements of 1st list are the keys and 
# the elements of the 2nd list are the corresponding values.
a1=["one","two","three","four","five"]

b2=[1,2,3,4,5,]
n={}
for i in range(len(b2)):
   n.update({a1[i]:b2[i]})
print(n)


m=["divya","sable","manisha","vidya"]
n=[1,2,3,4,]
b={}
for i in range(len(n)):
       b.update({m[i]:n[i]})
print(b)

i=0
while i<10:
   print(i+1)
   i=i+2

   