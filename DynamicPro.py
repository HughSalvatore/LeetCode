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

    # 前序遍历
    def printPreOrder(self):
        if self.root == None:
            print("The binary tree is not existed")
        else:
            stack = list()
            outputlist = list()
            popNode = self.root
            while len(stack) or popNode != None:
                if popNode is None:
                    popNode = stack.pop().right
                    continue

                while popNode.left != None:
                    stack.append(popNode)
                    outputlist.append(popNode.element)
                    # print(popNode.element)
                    popNode = popNode.left
                    
                outputlist.append(popNode.element)
                # print(popNode.element)
                popNode = popNode.right
            print(outputlist)

    # 中序遍历
    def printMediumOrder(self):
        if self.root is None:
            print("The binary tree is not existed.")
        else:
            stack = list()
            outputlist = list()
            popNode = self.root
            while len(stack) or popNode != None:
                while popNode.left is not None:
                    stack.append(popNode)
                    popNode = popNode.left

                outputlist.append(popNode.element)

                popNode = stack.pop()
                outputlist.append(popNode.element)

                popNode = popNode.right
            print(outputlist)            
    
    # 后续遍历
    def printPostOrder(self):
        if self.root == None:
            print("The binary tree is not existed.")
        else:
            stack = list()
            outputlist = list()
            popNode = self.root
            while len(stack) or popNode != None:
                if popNode is None:
                    popNode = stack.pop().left
                    continue

                while popNode.right is not None:
                    stack.append(popNode)
                    outputlist.append(popNode.element)
                    popNode = popNode.right
                outputlist.append(popNode.element)
                popNode = popNode.left

            print(outputlist[::-1])
                

                

                    
               
                
if __name__ == "__main__":
    arr = [1, 4, 2, 8, 5, 7]
    bTree = BinaryTree()
    for i in arr:
        bTree.insertNodeInOrder(i)  
    # bTree.printBinaryTree()
    # bTree.printPreOrder()  
    # bTree.printPostOrder()
    bTree.printMediumOrder()
    
