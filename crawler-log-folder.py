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
