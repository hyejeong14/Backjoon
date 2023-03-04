import sys
N,M = map(int,input().split())
lst1=[i+1 for i in range(N)]
for idx in range(M):
    i,j = map(int,sys.stdin.readline().split())
    ball=lst1[i-1]
    lst1[i-1]=lst1[j-1]
    lst1[j-1]=ball
print(*lst1)