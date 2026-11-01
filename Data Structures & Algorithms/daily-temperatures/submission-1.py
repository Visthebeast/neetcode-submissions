class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        out = [0] * len(temperatures)
        stack = []  # stores pairs of (index, temperature)

        for i, val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                prev_i, _ = stack.pop()
                out[prev_i] = i - prev_i
            stack.append((i, val))

        return out