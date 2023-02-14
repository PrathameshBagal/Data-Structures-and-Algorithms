class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.next=None
        

class LinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    
    def __iter__(self): # Helps in iterating LL
        currNode=self.head
        while currNode:
            yield currNode.val
            currNode=currNode.next
    

class Queue:
    def __init__(self) -> None:
        self.ll=LinkedList()

    def __str__(self) -> str:
        values=[str(x) for x in self.ll]
        return ' '.join(values)

    def enqueue(self,val):
        currNode=Node(val)
        if self.ll.head is None:
            self.ll.head=currNode
            self.ll.tail=currNode
        else:
            self.ll.tail.next=currNode
            self.ll.tail=currNode

    def dequeue(self):
        if self.ll.head is None:
            print("Queue is empty.")
            return
        else:
            self.ll.head=self.ll.head.next

    
        

queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue)

queue.dequeue()

print(queue)