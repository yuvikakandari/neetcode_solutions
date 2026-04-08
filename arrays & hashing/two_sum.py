class Solution:
    def twoSum(self,A,target):
        hashmap={}
        for i, n in enumerate(A):
            c=target-n
            if c in hashmap:
                return(hashmap[c], i)
            hashmap[n]=i
        
"""
Approach:
create a hashmap.
numbers of list will be mapped to their index
traverse through the list, check if target in hashmap.
if target found, return index, if not, add it to hashmap
"""