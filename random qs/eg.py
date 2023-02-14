x = int(input())
y = int(input())
z = int(input())
n = int(input())
i,j,k=0,0,0
sum=0
for i in range(x+1) and j in range(y+1) and k in range(z+1):
    if i+j+k!=0:
        print(i,j,k)
    i+=1 
    j+=1
    k+=1    
    
    