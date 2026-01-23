H,S1,V,L,K,n=input().split(" ")
H=float(H)
S1=float(S1)
V=float(V)
L=float(L)

K=float(K)
n=int(n)
a=0

t1=(((H-K)*2)/10)**0.5
t2=((H*2)/10)**0.5
x1=S1+L-t1*V+0.00001
x2=S1-t2*V-0.00001

for i in range(n):
    if i<=x1 and i>=x2:
        a=a+1
print(a)