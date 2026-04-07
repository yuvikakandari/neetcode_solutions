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
    
"""
Approach:
anagram means that both sets must be of same length and set t must consist of same characters as set s and in the same frequnecy.
first we create hash maps of both sets.
we then compare frequency of each character in their hashmaps.
in the hashmap, the key is the character, the value is its frequency of occurance.
.get()is used to give us a default valjue incase specified key does not exist
"""