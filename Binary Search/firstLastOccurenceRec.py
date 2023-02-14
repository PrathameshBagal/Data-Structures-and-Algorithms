def findFirstOccurences(arr,key,l,r,flag):
    if l>r:
        if flag:
            return l
        else:
            return -1
    mid=l+(r-l)//2
 
    if arr[mid]==key:
        flag=True
    if arr[mid]>=key:
        ans=findFirstOccurences(arr,key,l,mid-1,flag)
    else:
        ans=findFirstOccurences(arr,key,mid+1,r,flag)
    return ans

def findLastOccurences(arr,key,l,r,flag):
    if l>r:
        if flag:
            return r
        else:
            return -1
    mid=l+(r-l)//2
    
    if arr[mid]==key:
        flag=True
        ans=findFirstOccurences(arr,key,mid+1,r,flag)
    elif arr[mid]<key:
        ans=findLastOccurences(arr,key,mid+1,r,flag)
    else:
        ans=findLastOccurences(arr,key,l,mid-1,flag)
    return ans


arr=[1,2,2,3,3,3,5,6,7,7,8]
l=0
r=10

flag=False
print(findFirstOccurences(arr,7,l,r,flag))
print(findLastOccurences(arr,7,l,r,flag))