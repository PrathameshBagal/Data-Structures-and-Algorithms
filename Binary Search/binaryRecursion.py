
def binarySearch(arr,l,r,key):
    if l>r:
        return -1
    mid=l+(r-l)//2
    if arr[mid]==key:
        return mid
    elif arr[mid]>key:
        ans=binarySearch(arr,l,mid-1,key)
    else:
        ans=binarySearch(arr,mid+1,r,key)
    return ans
arr=[1,3,4,6,8,9,14]
print(binarySearch(arr,0,(len(arr)-1),15))
    