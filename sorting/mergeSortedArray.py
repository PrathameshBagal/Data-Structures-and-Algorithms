def mergeSortedArr(nums1,nums2,m,n):
    if m==0:
        nums1=nums2
        return nums1
    max1,max2=m-1,n-1
    for i in range(len(nums1)-1,-1,-1):
        
        if max2==-1 or max1==-1:
            return nums1
        
        if nums1[max1]>=nums2[max2]:
            nums1[i]=nums1[max1]
            max1-=1
        else:
            nums1[i]=nums2[max2]
            max2-=1

    return nums1

# nums1=[1,2,9,0,0,0]
# nums2=[2,5,6]
nums1=[]
nums2=[1]
print(mergeSortedArr(nums1,nums2,0,1))