n=int(input())
def is_prime(n):
    ct=0
    for i in range(1,n+1):
        if n%i==0:
            ct+=1
    if ct==2:
        return True
    else:
        return False
l=[i for i in range(1,n+1) if is_prime(i)]
print(l)