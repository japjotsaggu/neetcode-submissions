class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x== 0: return 0 
            # if x == 1: return 1 
            if n == 0: return 1

            res = helper(x, n//2)
            return res * res * x if n%2 else res*res

        result = helper(x, abs(n)) 
        return result if n>=0 else 1/result