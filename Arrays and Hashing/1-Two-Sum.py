"""
find if difference is in hashmap, if not then store value in hashmap, do not use duplicate indices to calculate sum, remember you are looking for the difference in the hashmap"""

# create a hashmap
# check if the needed number is in hashmap
    # if present, return the index
    # if not present, add current number and it's index to hashmap

# time: O(n)
# space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for index, value in enumerate(nums):
            
            if (target-value) in hashmap:
                return [index, hashmap[target-value]]
            
            hashmap[value] = index
        

        