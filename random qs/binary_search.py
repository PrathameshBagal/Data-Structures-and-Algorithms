
def binary_search(n,list,item):
    l=0
    location=-1
    u=n-1 
    if l<=u:
        mid=(l+u)//2
        if list[mid]==item:
            return mid
              
        elif list[mid]<item:
            l=mid+1
        else:
            u=mid-1        
    if l==u:
        return mid
    return None

def binary_search2(list,item,l,u):
    while l<=u:
     mid1=(l+(u-l))//2
     if list[mid1]==item:
        return mid1
     elif list[mid1]<item:
        return binary_search2(list,item,mid1+1,u)    
     elif list[mid1]>item :
        return binary_search2(list,item,l,mid1-1)    
    
              




list=[]
n=int(input("Enter the length of the array:"))
for i in range(n):
    elements=int(input("Enter number in the list:"))
    list.append(elements)
item=int(input("enter no. to be found:"))
print(binary_search(n,list,item))
# print(binary_search2(list,item,0,n-1))  Gives an error if item not in list