import sys

N,M=map(int,input().split())
lst1=[0 for i in range(N)]

for idx in range(M):
    i,j,k=map(int,sys.stdin.readline().split())
    for idx2 in range(i-1,j):
        lst1[idx2]=k

print(*lst1)