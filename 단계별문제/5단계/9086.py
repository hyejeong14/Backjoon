import sys
N=int(input())
for i in range(N):
    str=sys.stdin.readline().rstrip()
    strlist=list(str)
    print(strlist[0]+strlist[-1])