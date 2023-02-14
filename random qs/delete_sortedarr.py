def binarySearch(arr,key):
    l=0
    r=len(arr)-1
    
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==key:
         return mid
        elif arr[mid]>key:
         r=mid-1
        elif arr[mid]<key:
         l=mid+1
    return -1         
        
    
        

def deleteKey(arr,key):
    loc=binarySearch(arr,key)
    if loc==-1:
        return len(arr)
    
    for i in range(loc,(len(arr)-1)):
        arr[i]=arr[i+1]    
    return (len(arr)-1)    




arr=[1,3,5,9,11,13]
key=13
n=deleteKey(arr,key)
print(arr[:n])
# print(binarySearch(arr,key))