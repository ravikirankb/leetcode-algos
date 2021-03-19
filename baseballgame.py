class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []
        c = 0
        for v in ops:
            if v == "+":
                result.append(result[c -1] + result[c -2])
                
            elif v == "D":
                result.append(2 * result[c -1])
                
            elif v == "C":
                result.pop()
                c -= 1
                continue
            else:
                result.append(int(v))
            c += 1
        return sum(result)
