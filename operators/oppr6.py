class Solution:
    def utility(self, a, r, n):
        # code here 
        ans = a*(r**(n-1))
        # Print the ans
        print (ans)
        
s = Solution()
a = int(input("Enter the first term:"))
r = int(input("Enter the common difference:"))
n = int(input("Enter the term:"))
s.utility(a,r,n)
