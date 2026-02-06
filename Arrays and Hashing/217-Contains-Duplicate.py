"""
use a hashset to check for duplicates quickly

"""


# create set
# loop through input check if element in set
    # if in set return True
    # it not in set, add to set
# return False if no duplicate

# time: O(n)
# space: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for val in nums:
            if val in hashset:
                return True
            
            hashset.add(val)
        
        return False
        