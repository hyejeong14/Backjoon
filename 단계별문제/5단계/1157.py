s=list(input().upper())
ss=list(set(s))

result=[]

for i in ss:
    cnt=s.count(i)
    result.append(cnt)


M=max(result)
cnt=result.count(M)
if cnt==1:
    idx=result.index(max(result))
    print(ss[idx])
else:
    print("?")

