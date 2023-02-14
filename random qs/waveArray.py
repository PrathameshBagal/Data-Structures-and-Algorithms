'''input=[1,2,3,4,5]
expected output=[2,1,4,3,5]'''

def waveArray(arr,n):
    for i in range(0,n,2):
        arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr    

print(waveArray([2,4,7,8,9,10],6))