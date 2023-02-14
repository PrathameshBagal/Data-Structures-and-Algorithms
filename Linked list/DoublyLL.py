from hashlib import new


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def prepend(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
            newnode.next=None
            newnode.prev=None
            return
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode
    def append(self,data):
        newnode=Node(data)
        if self.tail is None: #check empty list
            self.head=newnode
            self.tail=newnode
            return
        newnode.prev=self.tail
        self.tail.next=newnode
        self.tail=newnode
    def insertBefore(self,data,ref):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
            return
        if ref==self.head:
            self.prepend(data)
            return
        newnode.prev=ref.prev
        ref.prev=newnode
        newnode.next=ref
        newnode.prev.next=newnode  
    def insertAfter(self,data,ref):
        if ref==self.tail:
            self.append(data)
            return
        newnode=Node(data)
        newnode.next=ref.next
        ref.next=newnode
        newnode.prev=ref
        newnode.next.prev=newnode
    
    def insertLocation(self,data,location):
        newnode=Node(data)
        temp=self.head
        index=0
        if location>=self.get_length() or location<0:
            print("Location out of index")
            return
        if location==0:
            self.prepend(data)
            return
        while index<location-1 and temp:
            temp=temp.next
            index+=1
        newnode.prev=temp
        newnode.next=temp.next
        temp.next=newnode
        newnode.next.prev=newnode

    def reverseTraversal(self):
        if self.head is None:
            print("List is empty")
            return
        temp=self.tail
        while temp:
            print(temp.data,end=' ')
            temp=temp.prev
    def del_beg(self):
        if self.head is None:
            print("List is empty")
            return
        self.head=self.head.next
        self.head.prev=None
    def del_end(self):
        if self.tail is None:
            print("LL is empty")
            return
        last=self.tail.prev
        last.next=None
    
    def delAtLocation(self,location):
        if location==0:
            self.del_beg()
            return
        temp=self.head
        index=0
        while index<location-1:
            temp=temp.next
            index+=1
        nextnode=temp.next.next
        temp.next=nextnode
        nextnode.prev=temp
    
    def delEntireLL(self):
        if self.head is None:
            return
        temp=self.head
        while temp:
            temp.prev=None
            temp=temp.next
        self.head=None
        self.tail=None


      
    def printDLL(self):
        if self.head is None:
            print("The list is empty")
            return
        node=self.head
        while node:
            print(node.data,end=' ')
            node=node.next
    def get_length(self):
        length=0
        if self.head is None:
            return 0
        node=self.head
        while node:
            length+=1
            node=node.next
        return length

dll1=DLL()
dll1.append(14)
dll1.prepend(5)
dll1.prepend(8)
dll1.prepend(11)
dll1.prepend(13)
dll1.append(0)
dll1.insertBefore(99,dll1.head)
dll1.insertAfter(100,dll1.head.next)
dll1.insertLocation(200,4)
dll1.printDLL()
print('\n')
dll1.del_beg()
dll1.printDLL()
print('\n')
dll1.del_end()
dll1.printDLL()
print('\n')
dll1.delAtLocation(5)
dll1.printDLL()
print("\n")
dll1.delEntireLL()
dll1.printDLL()
print('\n')
# dll1.reverseTraversal()
print('The length of LL is ',dll1.get_length())