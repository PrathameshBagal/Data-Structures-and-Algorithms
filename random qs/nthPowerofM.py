'''
if n==1:
    return m
power_nth=m*power(n-1)th
'''
def powerOfM(m,n):
    assert n>0 and n==int(n),'N has to be a positive integer'
    
    if n==1:
        return m
    return m*powerOfM(m,n-1)    

print(powerOfM(5,4))