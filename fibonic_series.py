def fibonacci(n):
        i=0
        j=1
        if n==1:
            print(i,end="")
        else:
            print(i,end=" ")
            for l in range(n-1):
                k=i
                i=j
                j=j+k
                print(i,end=" ")
fibonacci(4)