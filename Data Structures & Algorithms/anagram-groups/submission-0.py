class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for ace in strs:
            key = "".join(sorted(ace))
            if key not in dic:
                dic[key]=[]
            dic[key].append(ace)
        return list(dic.values())