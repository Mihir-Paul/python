class Solution:

    def findAnswer(self, d, n):
        x = n % 7
        ans = d - x
        if ans >= 0:
            return ans
        else:
            return 7 + ans


f = Solution()
print(f.findAnswer(2,19))