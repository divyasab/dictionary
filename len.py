# a={"divya":10,"sejal":30,"vidya":50}
# print(a)
# n=len(a)
# print(n)

a={"divya":10,"kavita":15,"vidya":10}
b={}
for i in a:
    if a[i] not in b:
        b.update(a[i])
print(b)