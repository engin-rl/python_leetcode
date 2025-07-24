class TwoSum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
            
    def twoSum(self):
        for i in range(len(self.nums)):
            current_sum = 0
            for j in range(len(self.nums)):
                if i != j:
                    current_sum = self.nums[i] + self.nums[j]
                    if current_sum == self.target:
                        return list([i, j])

if __name__ == "__main__":
    cases = [TwoSum([2, 7, 11, 15], 9), TwoSum([3, 2, 4], 6), TwoSum([3, 3], 6)]
    for case in cases:
        print(case.twoSum())



'''
for leetcode

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        for i in range(len(self.nums)):
            current_sum = 0
            for j in range(len(self.nums)):
                if i != j:
                    current_sum = self.nums[i] + self.nums[j]
                    if current_sum == self.target:                        
                        return list([i, j])


'''