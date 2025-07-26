import numpy as np


class Palindrome:
    def turnIntIntoArray(self, x):
        turnedString = str(x)
        turnedArray = [char for char in turnedString]
        return turnedArray

    def howLongStr(self, x):
        howLong = len(str(x))
        return howLong

    def getArrayParts(self, x):
        turnedArray = self.turnIntIntoArray(x)
        howLong = self.howLongStr(x)
        leftArray = turnedArray[0 : int(howLong / 2)]
        rightArray = list(reversed(turnedArray[int(howLong / 2) : int(howLong)]))
        if len(leftArray) != len(rightArray):
            rightArray.pop()
        return leftArray, rightArray

    def isPalindrome(self, x):
        leftArray, rightArray = self.getArrayParts(x)
        npLeft = np.array([leftArray])
        npRight = np.array([rightArray])
        checkPalindrome = (npLeft == npRight).all()
        return checkPalindrome


if __name__ == "__main__":
    cases = [121, -121, 10]
    for case in cases:
        print(Palindrome().isPalindrome(case))


"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
"""
