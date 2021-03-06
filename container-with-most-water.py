class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
		    l = len(height) - 1, r = 0

		    while l < r:
          area = (r - l) * min(height[l], height[r])
          maxarea = max(maxarea, area)

          if height[l] < height[r]:
            l += 1
          else:
            r -= 1

		    return maxarea
