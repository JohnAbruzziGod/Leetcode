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
        
        last, i = 0, 1
        num = 1
        while i < len(A):
            if num < 2:
                if A[last] == A[i]:
                    num += 1
                
                last += 1
                A[last] = A[i]
            else:
                num = 1
            
            i += 1
        print (A)    
        return last + 1
        
        

if __name__ == "__main__":
    print (Solution().removeDuplicates([1,1,1,2,2,2,3]))
    