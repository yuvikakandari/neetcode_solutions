class Solution:
    def isAnagram(self, s, t):
        countS={}
        countT={}
        if len(s)!=len(t):
            return (False)
        for i in range(len(s)):
            countS[s[i]]=countS.get(s[i],0)+1
            countT[t[i]]=countT.get(t[i],0)+1
        for a in countS:
            if countS[a]!=countT.get(a,0):
                return (False)
        return (True)