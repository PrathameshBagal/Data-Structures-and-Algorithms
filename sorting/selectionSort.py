def selection(list):
    for i in range(len(list)):
        minI=i
        for j in range(i,len(list)):
            if list[j]<list[minI]:
                minI=j
            list[minI],list[i]=list[i],list[minI]
    return list

def selectionRec(list,start):
    if start==len(list)-1:
        return list
    minI=start
    for i in range(start,len(list)):
        if list[i]<list[start]:
            minI=i
    list[start],list[minI]=list[minI],list[start]

    ans=selectionRec(list,start+1)
    return ans



list=[2,5,3,2,5,3,9,4]
print(selection(list))
print(selectionRec(list,0))