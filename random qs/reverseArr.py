def reverseArray(a,start,end):
    
    if start>=end:
        return a
    a[start],a[end]=a[end],a[start]
    
    return reverseArray(a,start+1,end-1)
    
print(reverseArray([1,2,3],0,2)    )


def revArr(a):
    n=len(a)
    ans=[]
    for i in range(n-1,-1,-1):
        ans.append(a[i])
    return ans    
print(revArr([1,2,3,4]))        