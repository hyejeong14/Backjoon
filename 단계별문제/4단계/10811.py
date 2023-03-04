import sys
N,M=map(int,input().split())
lst1=[num for num in range(1,N+1)]
lst2=[]

for idx in range(M):
    i,j=map(int,sys.stdin.readline().split())
    lst2=lst1[i-1:j]
    lst2.reverse()
    lst1[i-1:j]=lst2

print(*lst1)