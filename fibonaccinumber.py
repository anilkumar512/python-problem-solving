def Nf(n):
    if n<=1:
        return n
    return Nf(n-1)+Nf(n-2)

n=int(input())
print(Nf(n))