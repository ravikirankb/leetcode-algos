class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None or len(height) == 0:
            return 0
        
        l_max,r_max,l,r,ans = 0,0,0,len(height) -1,0
        
        while l < r:
            if height[l] < height[r]:
                if height[l] >= l_max:
                    l_max = height[l]
                else:
                    ans += (l_max - height[l])
                l = l + 1
            else:
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    ans += (r_max - height[r])
                r = r -1
                  
        return ans
