class StackInArray:
    def __init__(self,k,n):
        self.free=0
        self.k=k
        self.n=n
        self.arr=[0]*self.n
        self.top=[-1]*self.k
        self.next=[None]*n
        for i in range(self.n -1):
            self.next[i]=i+1 
        self.next[-1]=-1
        #print(self.arr,self.next)

    def push(self,ele,sN):
        if self.free==-1:
            #print(-1)
            return -1
        insertPos=self.free
        self.free=self.next[insertPos]
        self.arr[insertPos]=ele
        self.next[insertPos]=self.top[sN-1]
        self.top[sN-1]=insertPos
        #print(self.arr,self.top,self.next)
        return 1

    def pop(self,sN):
        if self.top[sN-1]==-1:
            print(-1)
            return -1
        popI=self.top[sN-1]
        ans=self.arr[popI]
        self.arr[popI]=None
        self.free=popI
        self.top[sN-1]=self.next[popI]
        self.next[popI]=popI

        print(ans)
        #print(self.arr,self.top,self.next)
        return
    def printList(self):
        print(self.arr,self.top)
        return

st=StackInArray(4,10)
st.push(1,1)
st.push(2,1)
st.push(3,1)
st.push(4,2)
st.push(1,1)
st.push(2,1)
st.push(3,1)
st.push(4,2)
st.push(1,1)
st.push(2,1)
st.printList()
st.pop(1)
st.pop(2)
st.printList()
st.push(7,2)
st.printList()
st.pop(2)
st.pop(1)
st.printList()
