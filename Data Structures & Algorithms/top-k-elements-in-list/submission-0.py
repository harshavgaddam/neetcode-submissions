class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store={}
        for i in nums:
            store[i]=store.get(i,0)+1

        sorte= sorted(store, key = store.get, reverse=True)
        return sorte[:k]