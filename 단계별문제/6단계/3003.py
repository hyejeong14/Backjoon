N=list(input().split(" "))
p=[1,1,2,2,2,8]
for i in range(len(N)):
    p[i]=p[i]-int(N[i])

print(*p)