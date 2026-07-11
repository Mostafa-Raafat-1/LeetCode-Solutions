"""
LeetCode 242 - Valid Anagram

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
- Hash Map
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s={}
        count_t={}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)): #O(n)
            count_s.setdefault(s[i], 0) #amortized O(1)
            count_t.setdefault(t[i], 0) #amortized O(1)
            count_s[s[i]] +=1
            count_t[t[i]] +=1
        
        return count_s == count_t # O(n)
