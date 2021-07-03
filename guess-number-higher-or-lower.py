# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,h = 0,n
        while (l<=h):
            mid = (l+h)//2
            result = guess(mid)
            if result == 0:
                return mid
            elif(result < 0):
                h = mid - 1
            else:
                l = mid + 1
        return -1
