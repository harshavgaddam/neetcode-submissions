class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val={}
        for i,j in enumerate(nums):
            diff = target-j
            if diff in val:
                return [val[diff], i]
            val[j]= i                 