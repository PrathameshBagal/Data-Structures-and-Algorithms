def factRecursion(n):
    if n==0 or n==1:
        return 1
    return n*factRecursion(n-1)    

n=int(input("Enter number for factorial:"))
print(factRecursion(n))


