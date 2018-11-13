import math

# find two numbers which their sum = target
def findTwoNumSum(array, target):
    array.sort()
    lenth = len(array)
    i = 0
    j = lenth - 1
    while (i < j):
        sum = array[i] + array[j]
        if sum == target:
            return (array[i], array[j])
        elif sum > target:
            j -= 1
        else:
            i += 1
    print("not found!\n")        
    return (-1, -1)

# Determine if a number is the sum of the squares of two int numbers
def isSquare(target):
    i = 0
    j = int(math.sqrt(target))
    while (i <= j):
        sumOfSquare = i * i + j * j
        if sumOfSquare == target:
            return True
        elif sumOfSquare > target:
            j -= 1
        else:
            i += 1
    
    return False

# Determine if a string is the palindrome, you only can delete one letter..
def isPalindrome(target, i, j):
    while i <= j:
        if target[i] == target[j]:
            i += 1
            j -= 1
            pass
        else:
            return False
    return True

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, new_data):
        self.val = new_data
    
    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class SingLinkList():
    def __init__(self):
        self.head = None
        self._length = 0

    def getLength(self):
        return self._length

    def isEmpty(self):
        return self.head == None

    def isLast(self, node):
        return node.get_next() == None

    def append(self, dataOrNode):
        item = None
        if isinstance(dataOrNode, ListNode):
            item = dataOrNode
        else:
            item = ListNode(dataOrNode)

        if self.head == None:
            self.head = item
            self._length += 1
        else:
            ref = self.head
            while ref.get_next():
                ref = ref.get_next()
            ref.set_next(item)
            self._length += 1

    def find(self, value):
        ref = self.head
        while ref != None and ref.get_data() != value:
            ref = ref.get_next()
        return ref

    def findprevious(self, value):
        ref = self.head
        while ref.get_next() != None and ref.get_next().get_data() != value:
            ref = ref.get_next()
        return ref
        

    def delete(self, value):
        toDelPreNode = self.findprevious(value)
        if toDelPreNode.get_next() != None:
            toDelPreNode.set_next(toDelPreNode.get_next().get_next())
            self._length -= 1

    def insert(self, value, position):
        targetNode = ListNode(value)
        targetNode.set_next(position.get_next())
        position.set_next(targetNode)
        self._length += 1

    def printLinkList(self):
        ref = self.head
        while ref != None:
            print(ref.get_data())
            ref = ref.get_next()
     

if __name__ == '__main__':
    # array = [1, 4, 2, 8, 5, 7]
    # (i, j) = findTwoNumSum(array, 12)
    # print(i, j)
    # print(isSquare(11))
    # print(isPalindrome("abba"))
    linklist = SingLinkList()
    for i in range(6):
        linklist.append(i)
    linklist.printLinkList()
    # print("deleted 2")
    # linklist.delete(2)
    # linklist.printLinkList()
    # print("delete 5")
    # linklist.delete(5)
    # linklist.printLinkList()
    targetNode = linklist.find(3)
    linklist.insert(9, targetNode)
    linklist.printLinkList()
    targetNode = linklist.findprevious(9)
    linklist.insert(10, targetNode)
    linklist.printLinkList()
    print(linklist.getLength())

