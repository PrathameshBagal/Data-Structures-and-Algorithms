class KQueues:
    def __init__(self,k,n) -> None:
        self.arr=[-1]*n
        self.next=[] 
        for i in range(n):
            self.next.append(i+1)
        self.next[-1]=-1
        self.free=0
        self.rear,self.front=[-1]*k,[-1]*k
    
    
    def printQ(self):
        print(self.arr)
        return
   
   
    def enqueue(self,qn,ele):
        qn-=1
        if self.free==-1:
            print("Q is full")
            return -1
        index=self.free
        if self.front[qn]==-1:
            self.front[qn]=index
        else:
            # Linking new ele to prev ele in same Q
            #by storing index of new ele of a Q as the next[i]
            # for the prev ele as if Q qn is popped, the new ele 
            #can be stored as head.
            self.next[self.rear[qn]]=index

        # As next[i] stores next free I when its empty
        self.free=self.next[index]

        self.rear[qn]=index
        self.arr[index]=ele
        self.next[index]=-1
        print("Next :",self.next)

    def deQueue(self,qn):
        qn-=1
        if self.front[qn]==-1:
            return "Queue is empty"
        popI=self.front[qn]
        # When arr[i] is filled, next[i] stores the index of 
        # next ele in the same Q hence we use it to update front[qn]
        self.front[qn]=self.next[popI]

        self.next[popI]=self.free
        self.free=popI
        print("DEQ Next :",self.next)
        return self.arr[popI]

q=KQueues(3,8)
q.enqueue(1,10)
q.enqueue(1,11)
q.enqueue(2,20)
q.enqueue(1,12)

q.printQ()
print(q.deQueue(1))
print(q.deQueue(1))
# print(q.deQueue(1))
# print(q.deQueue(1))
# print(q.deQueue(2))
# print(q.deQueue(2))
# q.printQ()
# q.enqueue(1,10) 