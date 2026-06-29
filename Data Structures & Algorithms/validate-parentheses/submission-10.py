class Solution:
    def isValid(self, s: str) -> bool:
        
        all_brackets = { ')': '(', '}':'{', ']': '['}
        
        closed = {')', '}', ']'}

        stack = []

        for i in range(len(s)):
            if s[i] not in closed:
                stack.append(s[i])
            elif s[i] in closed:
                if not stack:
                    return False
                elif stack[-1] == all_brackets.get(s[i]):
                    stack.pop()
                else:
                    stack.append(s[i])
                
        
        if not stack:
            return True
        else:
            return False
        

