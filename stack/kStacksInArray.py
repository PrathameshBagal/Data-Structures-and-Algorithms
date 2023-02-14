
# In this approach the memory usage is very poor as even if there is space
# in an array the particular stack might be full thus leading to inability to store new data

class KStacks:
    def __init__(self,k,n):
        self.k=k #number of stacks
        self.n=n # len of arr
        self.list=[None]*n
        rem=n%k
        self.sizes=[n//k]*k
        for i in range(rem):
            self.sizes[i]+=1
        # to maintain the top of each stack
        self.top=[-1]*k
        self.top[0]=0
        for i in range(1,k):
            self.top[i]=self.sizes[i-1]+self.top[i-1]
        
        # To count if a stack is empty
        #Accounts for free spots in each stack
        self.free=[]
        for i in (self.sizes):
            self.free.append(i)

    def push(self,ele,sN): #sN=stackNumber
        sN-=1
        if self.free[sN]>0:
            self.list[self.top[sN]]=ele
            self.top[sN]+=1
            self.free[sN]-=1
            #print(self.list)
            return True
        else:
            return -1
            #print(f"Stack Overflow for stack number {sN+1}")

    def pop(self,sN):
        sN-=1
        if self.free[sN]==self.sizes[sN]:
            #print(f"Stack number {sN+1} is already empty")
            return -1
        else:
            ans=self.list[self.top[sN]-1]
            self.top[sN]-=1
            self.free[sN]+=1
            #print(ans)
            return ans

    def printList(self):
        print(self.list)
        
st=KStacks(4,10)
st.push(1,1)
st.push(2,1)
st.push(10,2)
st.push(3,1)
st.push(4,1)
st.push(1,3)
st.push(1,3)
st.push(1,3)
st.printList()
st.pop(4)
st.pop(1)
st.pop(2)
st.push(10,4)
st.printList()