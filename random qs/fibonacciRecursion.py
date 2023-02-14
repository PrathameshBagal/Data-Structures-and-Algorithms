def fibRecursion(n):
    
    if n<=1:
        return n
    return fibRecursion(n-1)+fibRecursion(n-2)
    

n=5
# n=int(input("Enter n for fibonacci:"))
a=fibRecursion(4)
print(a)
