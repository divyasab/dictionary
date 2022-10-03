a={"divya":18,"sejal":36,"vidya":10}
# for i in a:
#     print(i,a[i])

# for i in a:
#     print(i)

for i in a.values():
    print(i)
for x,y in a.items():
    print(x,y)

# a=[23,54,67,78,4]
# i=0
# b=a[0]
# while i<len(a):
#     if a[i]<b:
#         b=a[i]
#     i=i+1
# print(b)


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
