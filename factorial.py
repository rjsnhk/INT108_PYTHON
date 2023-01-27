n=int(input())
def factorial(n):
    p=1
    for i in range(n,0,-1):
        p*=i
    return p
print(factorial(n))