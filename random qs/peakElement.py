def peakElement(arr, n):
        start=0
        end=n-1
        return binSearch(arr,start,end,n)
    
def binSearch(arr,start,end,len):
    
        while(start<=end):
            mid=(start+(end-start))//2
            if len==1:
                return 0
            if arr[0]>arr[1]:
                return 0
            if arr[len-1]>arr[len-2]:
                return len-1
            if arr[mid]<arr[mid-1]:
                end=mid-1
            if arr[mid]>arr[mid+1]:
                start=mid+1        
        return mid

print(peakElement([1,2,3,4,3,2],4))            