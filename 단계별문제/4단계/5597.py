import sys
lst1=[i for i in range(1,31)]
for i in range(28):
    n=int(sys.stdin.readline())
    lst1.remove(n)
print(min(lst1),max(lst1))