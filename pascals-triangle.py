## my simple O(n2) solution. Beats over 50% 
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        res.append([1])
        for i in range(1,numRows):
            p = res[i-1]
            v = []
            for j in range(0,i+1):
               sum = 0
               if j == 0:
                  v.append(p[0])
                  continue
               try:
                  sum += p[j-1]
                  sum += p[j]
               except Exception as e:
                  pass
               v.append(sum)
            res.append(v)

        return res
