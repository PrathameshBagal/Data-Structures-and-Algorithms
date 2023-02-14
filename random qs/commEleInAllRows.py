from collections import defaultdict

def findCommon(arr):
    n=len(arr)
    m=len(arr[0])
    unique={}
    for i in range(m):
        unique[arr[0][i]]=1
    

    for i in range(1,n):
        for j in range(m):
            if arr[i][j] in unique.keys() and unique[arr[i][j]]==i:
                unique[arr[i][j]]+=1
    for key in unique.keys():
        if unique[key]==n:
            print(key,end=' ')
    # return unique




arr=[[1, 2, 1, 4, 8],
[3, 1, 8, 5, 1],
[8, 7, 7, 3, 1],
[8, 1, 2, 7, 9],]

(findCommon(arr))

    # dict={}
    
    # for i in range(n):
    #     unique=set()
    #     for j in range(m):
    #         ele=arr[i][j]
    #         unique.add(ele)
    #         dict[i]=unique
    # return dict






