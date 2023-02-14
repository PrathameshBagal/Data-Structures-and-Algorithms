def sayDigits(num,ans,map):
    if num==0:
        return []

    dig=num%10
    num=num//10
    
    ans=sayDigits(num,ans,map)
    ans.append(map[dig])
    return ans


def sayDigits2(num,dig,map):
    if num==0:
        return dig

    dig=num%10
    num=num//10
    
    sayDigits2(num,dig,map)
    print(map[dig],end=" ")
    
    

map=["zero","one","two","three","four","five","six","seven","eight","nine"]
ans=[]
res=(sayDigits(412,ans,map))
res=" ".join(res)
print(res)
sayDigits2(412,0,map)