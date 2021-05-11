class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        
        i = 0
        while i < len(A) and K > 0:
                 if A[i] < 0:
                    A[i] = abs(A[i])
                    K -= 1
                    i += 1
                 else:
                    try:
                       if A[i-1] < A[i]:
                          A[i-1] = -A[i-1]
                          i -= 1
                       else:
                          A[i] = -A[i]
                    except:
                        A[i] = -A[i]
                    K -= 1
                        
                    
                    
        return sum(A)
                    
        
        
