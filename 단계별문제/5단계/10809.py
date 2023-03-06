s=list(input())
output=[i for i in range(ord('a'),ord('z')+1)]

for idx in range(len(output)):
    for idx2 in range(len(s)):
        if chr(output[idx])==s[idx2]:
            output[idx]=idx2
            break
        if chr(output[idx]) not in s:
            output[idx]=-1
            break
            
print(*output)