class Solution:
    def containsDuplicate(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True

            hashset.add(n)

        return False

"""
    Approach:
    Use a hash set to keep track of elements already seen.
    If an element already exists in the set, a duplicate is found.

    Time Complexity: O(n)
"""
