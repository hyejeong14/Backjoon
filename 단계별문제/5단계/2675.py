import sys
T=int(input())
for i in range(T):
    output=[]
    r,s=map(str,input().split())
    r=int(r);s=list(s)
    for j in range(len(s)):
        output.append(s[j]*r)
    print(*output,sep='')

