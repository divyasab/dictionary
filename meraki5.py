# # Write a program to remove duplicate keys.
# dic={"ball":"red",  "bat":4, "wickets":8, "ball":"green", "bat":3}
# temp = []
# res = dict()
# for key, val in dic.items():
#     if val not in temp:
#       temp.append(val)
#       res[key] = val
# print(res)


n=int(input("enter the number"))
d={}
for n in range(1,n+1):
      d.update({n:n**2})
print(d)
            
