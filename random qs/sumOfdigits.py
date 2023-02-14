def sumDig(n):
    if n<10:
        return (n) 
    return n%10 + sumDig((n//10))
    
print(sumDig(159))
