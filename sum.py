
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
for i in dic2:
    if i in dic1:
        dic2[i]=dic2[i]+dic1[i]
        print(dic2[i])
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
