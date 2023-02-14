class CQ:
    def __init__(self,maxSize):
        self.q=[None]*maxSize
        self.max=maxSize
        self.front,self.rear=-1,-1
        self.size=0
    
    def printQ(self):
        print(self.q)
        return

    def enQ(self,ele): 
        if self.size==self.max:
            return ("CQ is full")
        self.rear=(self.rear+1)%self.max
        if self.front==-1:
            self.front=0
        self.q[self.rear]=ele
        self.size+=1
        return self.q
    
    def deQ(self):
        if self.size==0:
            return ("CQ is empty")
        self.q[self.front]=None
        self.front=(self.front+1)%self.max
        self.size-=1
        return self.q

    def peek(self):
        print(self.q[self.front])

q= CQ(4)
(q.enQ(1))
(q.enQ(2))
(q.enQ(3))
(q.enQ(4))
(q.enQ(5))
(q.enQ(6))
(q.deQ())
q.deQ()
q.deQ()
q.enQ(5)

q.printQ()
q.peek()