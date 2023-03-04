import sys
N,X=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
list1=[]
for i in A:
    if X>i:
        list1.append(i)
print(*list1)