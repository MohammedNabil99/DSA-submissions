class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        character_count_s = {}
        character_count_t = {}
        for i in range(len(s)):
            character_count_s[s[i]] = 1 + character_count_s.get(s[i], 0)
            character_count_t[t[i]] = 1 + character_count_t.get(t[i], 0)
        return character_count_s == character_count_t
        

        