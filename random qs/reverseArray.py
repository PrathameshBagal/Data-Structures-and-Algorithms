def reverseArray(t,n,arr,start,end):
    iterations=n//2
    for i in range(iterations):
        if start<=end:
         arr[start],arr[end]=arr[end],arr[start]
         start+=1
         end-=1
    
     
        
def recursiveReverseArray(arr,start,end)   :
    if start<=end:
       arr[start],arr[end]=arr[end],arr[start]
       recursiveReverseArray(arr,start+1,end-1)
       
def reverseArray3(arr):
    return arr[::-1]
    
        
    

arr=[1,23,45,65,34,78,98]
n=len(arr)
start=0
end=n-1
# reverseArray(1,n,arr,start,end)
# for i in range(n):
#     print(arr[i],end=" ")
recursiveReverseArray(arr,start,end)
for i in range(n):
    print(arr[i],end=" ")
# print(reverseArray3(arr))