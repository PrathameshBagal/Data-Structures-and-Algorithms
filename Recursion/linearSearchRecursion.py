def linearSearch(arr,ele):
    if len(arr)==0:
        return False
    if arr[0]==ele:
        return True

    ans=linearSearch(arr[1:],ele)    
    return ans
    
arr=[1,2,3,4]
print(linearSearch(arr,-1))
