class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Go through the nums array
        # Find the sequences that exist
        # If there is no left neighbor, it means start of a sequence
        # use hashset to make sure the list is unique

        numSet = set(nums) # entire input array is stored in a set
        longest = 0

        for num in nums:
            if (num - 1) not in nums:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest

        #Time: O(N), going through the entire array
        #Space: O(N), using hashSet
        

        