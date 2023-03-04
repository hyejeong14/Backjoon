import sys
lst1=[]
for i in range(10):
    n=int(sys.stdin.readline())
    lst1.append(n%42)
lst2=[]
for i in lst1:
    if i not in lst2:
        lst2.append(i)

print(len(lst2))