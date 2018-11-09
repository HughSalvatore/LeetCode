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

if __name__ == '__main__':
    # array = [1, 4, 2, 8, 5, 7]
    # (i, j) = findTwoNumSum(array, 12)
    # print(i, j)
    print(isSquare(11))