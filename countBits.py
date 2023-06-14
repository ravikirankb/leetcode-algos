class Solution:
    def countBits(self, n: int) -> List[int]:
        ans =[]
        for i in range(0,n):
            res = str(bin(i))
            ans.append(res.count('1'))
        return ans
