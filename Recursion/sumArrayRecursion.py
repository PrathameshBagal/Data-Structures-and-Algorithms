def sumArray(arr ):
    if len(arr)==1:
        return arr[0]
    sum=arr[0]
    sum+=sumArray(arr[1:])
    return sum

def sumArray2(arr ):
    if len(arr)==1:
        return arr[0]
    
    sum=sumArray(arr[1:])
    sum+=arr[0]
    return sum

arr=[1,2,3,4]
print(sumArray2(arr))
# print(sumArray(arr))