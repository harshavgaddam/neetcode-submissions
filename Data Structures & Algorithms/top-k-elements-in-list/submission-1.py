class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store={}
        for i in nums:
            store[i]=store.get(i,0)+1
        bucket = [[] for a in range(len(nums)+1 )]
        for number,frequency in store.items():
            bucket[frequency].append(number)

        result=[]
        for frequency in range(len(bucket)-1,0,-1):
            for number in bucket[frequency]:
                result.append(number)
                if len(result) == k:
                    return result
