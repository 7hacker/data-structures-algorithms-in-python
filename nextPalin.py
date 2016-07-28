def nextPalindrome(num):
    length=len(str(num))
    oddDigits=(length%2!=0)
    leftHalf=getLeftHalf(num)
    middle=getMiddle(num)
    if oddDigits:
        print("Odd!")
        increment=pow(10, length/2)
        newNum=int(leftHalf+middle+leftHalf[::-1])
        print("Increment: " + str(increment))
        print("newNum: " + str(newNum))
    else:
        print("Even!")
        increment=int(1.1*pow(10, length/2))
        newNum=int(leftHalf+leftHalf[::-1])
        print("Increment: " + str(increment))
        print("newNum: " + str(newNum))
    if newNum > num:
        return newNum
    if middle!='9':
        return newNum+increment
    else:
        return nextPalindrome(roundUp(num))
 
def getLeftHalf(num):
    return str(num)[:len(str(num))/2]
 
def getMiddle(num):
    return str(num)[(len(str(num))-1)/2]
 
def roundUp(num):
    length=len(str(num))
    increment=pow(10,((length/2)+1))
    print("Round up!")
    print("Increment: " + str(increment))
    print("Result:" + str(((num/increment)+1)*increment))
    return ((num/increment)+1)*increment

print(nextPalindrome(1891))