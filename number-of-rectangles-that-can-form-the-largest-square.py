class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        dict = {}
        prev_min = -1
        for r in rectangles:
            cur_min = min(r[0],r[1])
            if cur_min >= prev_min:
                if cur_min in dict:
                    dict[cur_min] += 1
                else:
                    dict[cur_min] = 1
            prev_min = cur_min
           
        for key in sorted(dict.keys(),reverse=True):
           return dict[key]
