h=[7,4,8,2,9]
j=[11,3,7,12,18,14,16,21,2,26,30,8,42]
ans=[]
max=0

for i in range(len(j))  :
      if j[i]>max:
       max=j[i]
       ans.append(max)
       
    #    print(max)
        
print(ans)
print('n=',len(ans))