class RomanToInt:
    def romanToInt(self, s):
        self.s = s
        sum = 0
        old_value = 0
        romans = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        a = self.s
        for char in reversed(self.s):
            value = romans[char]
            if value < old_value:
                sum -= value
            else:
                sum += value
                old_value = value
        print(sum)


RomanToInt().romanToInt("CMLXXIII")

""" # someone did this better i guess?
def romanToInt(self, s: str) -> int:
        num=0
        a={'I':1,'V':5, 'X':10, 'L': 50, 'C': 100, 'D':500, 'M':1000}
        s=s.replace('IV',"IIII").replace("IX","VIIII")
        s=s.replace('XL',"XXXX").replace("XC","LXXXX")
        s=s.replace('CD',"CCCC").replace("CM","DCCCC")
        for char in s:
            num+=a[char]
        return num
"""


""" # leetcode structure
class Solution:
    def romanToInt(self, s: str) -> int:
"""
