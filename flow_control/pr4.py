class Solution:
    def fun(self, a):
        # code here
        if a>0:
            print("Positive")
        elif a==0:
            print("Zero")
        else:
            print("Negative")
            
s = Solution()
a = int(input("Enter a number:"))
s.fun(a)