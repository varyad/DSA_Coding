"""
use hashmap as a frequency table to check for occurence of each element. Can actually use one hashmap for both strings with one incrementing and one decrementing and check at end if 0
"""

# create frequency table
# +1 to freq table for each letter in string one
# -1 to freq table for each letter in string two
# if a frequency value for a letter is 0, remove it 
# check if frequency table it empty
    #return True
    # else return False

# time: O(n)
# space: O(n) actually O(1) because at most 26 different letters


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = {}

        if len(s) != len(t):
            return False

        for index in range(len(s)):
            if s[index] in frequency:
                frequency[s[index]] +=1
            else:
                frequency[s[index]] = 1

            if t[index] in frequency:
                frequency[t[index]] -=1
            else:
                frequency[t[index]] = -1
            
            if s[index] in frequency and frequency[s[index]] == 0:
                frequency.pop(s[index])
            
            if t[index] in frequency and frequency[t[index]] == 0:
                frequency.pop(t[index])

        if not frequency:
            return True
        else:
            return False

            