


def insertKey(arr,cap,n,key):
    if n>=cap:
        return n
    i=n-1    
    while i>=0 and arr[i]>key:
        arr[i+1]=arr[i]
        i-=1    
    arr[i+1]=key    
    return (n+1)    

arr=[1,3,5,9,11]
for i in range(20):
    arr.append(0)
cap=len(arr)
n=5
key=7
n=insertKey(arr,cap,n,key)

print(arr[0:n])