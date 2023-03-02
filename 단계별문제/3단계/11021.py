import sys

T=int(input())
for i in range(T):
    a,b=map(int,sys.stdin.readline().split())
    str='Case #{0}'.format(i+1)
    print(str+":",a+b)