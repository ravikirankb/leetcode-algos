class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for s in logs:
            if s == "../":
               if len(stack) > 0 :
                    stack.pop()
            elif s == "./":
                continue
            else:
                stack.append(s)
                
                
        return len(stack)

    
   
# memory efficient
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps =0;
        for log in logs:
            if log == "../":
                if steps > 0:
                   steps -= 1
            elif log == "./":
                continue
            else:
                steps += 1
        return steps
