class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = [];
        for i in range(len(logs)):
            curr = logs[i]
            if(curr == "../"):
                if(len(stack) != 0):
                    stack.pop()
                continue;
            elif(curr == "./"):
                continue;
            else:
                stack.append(curr);
        return len(stack)