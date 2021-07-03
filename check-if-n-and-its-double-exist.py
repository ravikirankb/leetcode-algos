class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i,a in enumerate(arr):
            m = a * 2
            d = a / 2
            if m in arr[:i] or d in arr[:i]:
                return True
        
        return False
