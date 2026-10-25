class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for x in nums:
            if x in hash:
                return True
            hash.add(x)
        return False

        