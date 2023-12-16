class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        dictt = {}
        for i in s :
            dicts[i] = s.count(i)
        for j in t : 
            dictt[j] = t.count(j)
        return dicts == dictt 