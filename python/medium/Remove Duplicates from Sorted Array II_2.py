# Time:  O(n)
# Space: O(1)
#
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# 
# For example,
# Given sorted array A = [1,1,1,2,2,3],
# 
# Your function should return length = 5, and A is now [1,1,2,2,3].
#

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        
        last = 0
        index = 0
        B=[0,0,0,0,0,0,0,0]
        for value in A:
            index_2 = last-2
            if last < 2 or value > B[last-2]:
                B[last] = value
                last += 1
            index += 1
        return last
        

if __name__ == "__main__":
    print (Solution().removeDuplicates([1,2,2,2,2,3,3,3,4,5]))
    
    