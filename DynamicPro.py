class BTreeNode:
    def __init__(self, element=None):
        self.element = element
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, treeNode=None):
        self.root = treeNode

    def insertNodeInOrder(self, element):
        Node = BTreeNode(element)
        if self.root == None:
            self.root = Node
        else:
            queue = list()
            queue.append(self.root)
            
            while len(queue):
                popNode = queue.pop(0)
                if popNode.left == None:
                    popNode.left = Node
                    break
                elif popNode.right == None:
                    popNode.right = Node
                    break
                else:
                    queue.append(popNode.left)
                    queue.append(popNode.right)
    
    def printBinaryTree(self):
        if self.root is None:
            print("The binary tree is not existed.")
        else:
            queue = list()
            queue.append(self.root)

            while len(queue):
                popNode = queue.pop(0)
                print(popNode.element)
                if popNode.left != None:
                    queue.append(popNode.left)
                if popNode.right != None:
                    queue.append(popNode.right)
    

if __name__ == "__main__":
    arr = [1, 4, 2, 8, 5, 7]
    bTree = BinaryTree()
    for i in arr:
        bTree.insertNodeInOrder(i)
    
    bTree.printBinaryTree()

    
