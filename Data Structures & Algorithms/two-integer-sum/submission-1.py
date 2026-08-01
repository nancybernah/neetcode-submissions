class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i,j]
                    return[]