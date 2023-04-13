class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        for i in pushed:
            stack.append(i)
            while j < len(popped) and stack and popped[j] == stack[-1]:
                stack.pop()
                j += 1
        return not stack
        