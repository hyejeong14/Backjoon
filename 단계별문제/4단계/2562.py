import sys
max=0
od=0
for i in range(9):
    n=int(sys.stdin.readline())
    if max<n:
        max=n
        od=i+1
print(max)
print(od)