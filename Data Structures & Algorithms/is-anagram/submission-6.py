class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        character_count = {}
        for ch in s:
            character_count[ch] = character_count.get(ch, 0) + 1
        for ch in t:
            if ch not in character_count or character_count[ch] == 0:
                return False
            character_count[ch] -= 1
        return True

        