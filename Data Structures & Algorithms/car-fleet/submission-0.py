class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for i in range(len(position)):
            pair.append((position[i], speed[i]))

        pair.sort(key = lambda x:x[0], reverse=True)

        res = []

        for i in pair:
            t = (target-i[0])/i[1]
            # print(i)
            # print(t)
            if not res:
                res.append(t)
            elif t>res[-1]:
                res.append(t)
        
        return len(res)

