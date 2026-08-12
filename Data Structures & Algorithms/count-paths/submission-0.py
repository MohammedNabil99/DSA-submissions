class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n #bottom row is all set to 1

        for i in range (m-1):
            newRow = [1] * n #second to last row
            for j in range (n-2, -1, -1): #last column is all 1 so that's why start from second last to first (reverse order)
                newRow[j] = newRow[j + 1] + row[j] #compute right + down
            row = newRow #set row to newRow
        
        return row[0] #gets us the value at start index
        
        


        