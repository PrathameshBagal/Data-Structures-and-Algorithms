class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
class CSLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        currNode=self.head
        while currNode.next!=self.head:
            yield currNode.data
            currNode=currNode.next

    def prepend(self,data):
        newnode=Node(data)
        if self.head is None:
            newnode.next=newnode
            self.head=newnode
            self.tail=newnode
            return
        else:
            newnode.next=self.head
            self.head=newnode
            self.tail.next=newnode
    def append(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            self.head.next=newnode
            self.tail=newnode
            return
        newnode.next=self.head
        self.tail.next=newnode
        self.tail=newnode
    def insertAfter(self,data,ref_node):
        newnode=Node(data)
        if self.head is None:
           print("List is empty")
           return
        #if ref_node is at end
        if ref_node==self.tail:
            self.append(data)
            return
        newnode.next=ref_node.next
        ref_node.next=newnode
    def insertAtIndex(self,data,location):
        if location==0:
            self.prepend(data)
            return
        newnode=Node(data)
        index=0
        temp=self.head
        while index<location-1:
            index+=1
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
    
    def delBeg(self):
        if self.head!=None:
            self.head=self.head.next
            self.tail.next=self.head
    # delete at given index
    def deleteNode(self,location):
        if location==0:
            self.delBeg()
            return
        temp=self.head
        index=0
        while index<location-1:
            temp=temp.next
            index+=1
        temp.next=temp.next.next             
        

            
    
    def printlist(self):
        temp=self.head
        while temp.next:
            print(temp.data,end=' ')
            temp=temp.next
            if temp==self.head:
                break
            
list1=CSLL()
list1.prepend(1)
list1.prepend(2)
list1.prepend(3)
list1.prepend(4)
list1.append(5)
list1.delBeg()
list1.insertAfter(90,list1.tail)
list1.insertAtIndex(100,3)
# list1.printlist()
list1.deleteNode(0)
print("\n")
# list1.printlist()
print(list1)

