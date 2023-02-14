class TreeNode:
    def __init__(self,data) -> None:
        self.data=data
        self.leftChild,self.rightChild=None,None
    
newBt = TreeNode("Drink")
l1=newBt.leftChild= TreeNode("Hot")
r1=newBt.rightChild= TreeNode("Cold")
l1.leftChild=TreeNode("Tea")
l1.rightChild= TreeNode("Coffee")
r1.leftChild= TreeNode("Coke")
r1.rightChild= TreeNode("Fanta")

def preOrderTraversal(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
print("PREORDER")
preOrderTraversal(newBt)

def inOrderTraversal(rootNode):
    if rootNode is None:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
print("INORDER")
inOrderTraversal(newBt)

def postOrderTraversal(rootNode):
    if rootNode is None:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

print("POSTORDER")
postOrderTraversal(newBt)
    
def leftViewBT(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    leftViewBT(rootNode.leftChild)

print("LEFT VIEW OF BT")
leftViewBT(newBt)