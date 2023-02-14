def dToB(n):
    assert type(n)==int,'Num must be int'
    if n<1:
        return 0
    return n%2+10*dToB(n//2)
print(dToB(12))
'''   for n=10  b=1010
          q    r
 10/2     5    0   prev(r)*10+r   (1010+0=1010)
5/2       2    1   prev(r)*10 + r (100+1=101)
2/2       1    0   prev(r)*10 + r (10+0=10)
1/2       0    1   
 '''