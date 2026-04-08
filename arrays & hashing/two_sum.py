class Solution:
    def twoSum(self,A,target):
        hashmap={}
        for i, n in enumerate(A):
            c=target-n
            if c in hashmap:
                return(hashmap[c], i)
            hashmap[n]=i
        