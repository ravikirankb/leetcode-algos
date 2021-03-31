## simple solution using set
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y = 0 ,0
        paths_visited ={(0,0)}
        
        for p in path:
            if p == 'N':
               y += 1
            if p == 'S':
                y -= 1
            if p == 'W':
                x -= 1
            if p == 'E':
                x += 1
                
            cur_path =(x,y)
            if cur_path in paths_visited:
                return True
            paths_visited.add(cur_path)
        
        return False
                
            
