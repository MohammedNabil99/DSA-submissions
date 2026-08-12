class Solution:
    #Let's assume that the input nums array is non-empty
    #The output needs to be an array of numbers that are at least k most frequent
    #Output can be in any order

    #Pseudocode
    #First, initialize a dictionary 
    #Write a for loop to iterate over the nums array
    #check the count of each number in the array, if it is not in dictionary 
    #then add it and update count,
    #if it is in dictionary, just update count
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, c in count.items():
            freq[c].append(num)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
