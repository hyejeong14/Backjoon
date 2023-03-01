H,M=map(int,input().split())
if M<45:
    if H==0:
        H=24
    H=H-1
    M=(60-45)+M
elif M>=45:
    H=H
    M=M-45
print(H,M)