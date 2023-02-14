class Node:   # create a node
    def __init__(self,data):
        self.next=None
        self.data=data
class SinglyLinkedList: # create a LL
    def __init__(self):
        self.head=None
    
    
    
    def push(self,new_data): # Adding at the beginning
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def insertAfter(self,prev_node,new_data):#add in the middle
        if prev_node is None:#check if prev node exists
            print("The prev node must be in LL")
            return

        #else create a new node and add it in the LL
        new_node=Node(new_data)
        new_node.next=prev_node.next 
        prev_node.next=new_node
    # add node at the end             
    def append(self,new_data): 
        new_node=Node(new_data)

        #check if head exists. if not then add newnode
        if self.head is None:
            self.head =new_node
            return
        #traverse to end to reach last
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node

    def printList(self):
        node=self.head
        while node:
            print(node.data,end=' ') #TRAVERSAL IN SLL
            node=node.next            
    #Search in LL
    def searchSLL(self,target):
        if self.head is None:
            return "List is empty"
        else:
            node=self.head
            while node:
                if node.data==target:
                    return node.data
                node=node.next    
            return "Target does not exist in LL"    
    def delNode(self,key):
        #Check if list is empty
        if self.head==None:
            print("List is empty")
        
        #Check if 1st node is key
        if self.head.data==key:
            self.head=self.head.next
            return
        #To delete in middle and last
        temp=self.head
        #We try to find prev element which explains while condition
        '''If we took while temp is true it would execute for last ele
        also which we dont want. since we calculate previous we want to stop
        traversal at second last'''
        while temp:
            if temp.next.data==key:#Compare for next so we have the previous
                temp.next=temp.next.next#we store prev just to do this
                break
            temp=temp.next
        print("Element not in list"    )

    def deleteEntireLL(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head=None    
    def delByIndex(self,location):
        if self.head is None:
            print("The list is empty")
        
        index=0
        temp=self.head
        '''if Location==0 loop wont run and index stays zero
          so prev val wont be assigned and will give error referenced before assignment
          so we make special case if location==0'''
        while temp and index<location-1:
            # prev=temp
            temp=temp.next
            index+=1
        
        if location==0:
            self.head=self.head.next
        else:
            temp.next=temp.next.next        
         


llist = SinglyLinkedList()
 
# Insert 6.  So linked list becomes 6->None
llist.append(6)
 
    # Insert 7 at the beginning. So linked list becomes 7->6->None
llist.push(7)
 
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
llist.push(1)
 
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
llist.append(4)
llist.push(1)
llist.push(1)
llist.push(1)
 
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
# llist.insertAfter(llist.head.next, 8)
# # print(llist.searchSLL(8))
# print('Created linked list is: ')
llist.printList()

# llist.delNode(1)
# print("List after deletion is:")
# llist.deleteEntireLL()
# llist.delByIndex(0)
print("\n")
llist.printList()

