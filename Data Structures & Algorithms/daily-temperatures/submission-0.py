class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0]*len(temperatures)
        for i,val in enumerate(temperatures):
            if i!=0:
                if temperatures[i-1]>=val:
                    stack.append((i,val))
                else:
                    while stack and (stack[-1][1]<val):
                        out[stack[-1][0]]=i-stack[-1][0]
                        stack.pop()
                    stack.append((i,val))
            else:
                stack.append((i,val))
        
        return out
