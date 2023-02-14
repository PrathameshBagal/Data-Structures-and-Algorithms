

class CQueue:
    def __init__(self,maxSize) -> None:
        self.q=  maxSize * [None]
        self.maxSize=maxSize
        self.start=-1
        self.top=-1
        
    
    def __str__(self) -> str:
        q=[str(x) for x in self.q]
        return " ".join(q)

    def isEmpty(self):
        if self.top==self.start==-1:
            return True
    
    def isFull(self):
        if (self.top +1)% self.maxSize==self.start:
            return True
        else:
            return False


    def enqueue(self,x):
        if self.isFull():
            return "Queue is already full."
        elif self.start==-1:
            self.start,self.top=0,0
            self.q[self.top]=x
            return "Val updated"
        else:
            self.top=(self.top+1)%self.maxSize
            self.q[self.top]=x
            return "Val updated"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is already empty"
        else:
            self.q[self.start]=None
            self.start= (self.start+1)%self.maxSize

    def peek(self):
        return self.q[self.start]

    def deleteQueue(self):
        self.q=self.maxSize*[None]

class CQueue2:
    def __init__(self,k):
        pass      
queue=CQueue(4)            
print(queue.isEmpty())
# print(queue)
(queue.enqueue(1))
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.dequeue()
queue.enqueue("a")
print(queue,"\n",queue.start,queue.top)
print(queue.peek())
queue.deleteQueue()
print(queue)