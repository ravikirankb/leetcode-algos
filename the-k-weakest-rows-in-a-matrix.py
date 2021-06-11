class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dict = {i:0 for i in range(len(mat))}
        for i,r in enumerate(mat):
            for c in r:
                if c == 1:
                    dict[i] += 1
                else:
                    break
                    
        dict = sorted(dict.items(),key = lambda item:(item[1],item[0]))
        return [dict[i][0] for i in range(k)]
