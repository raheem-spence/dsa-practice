class Solution:
    def isValid(self, s: str) -> bool:
        
        all_brackets = { ')': '(', '}':'{', ']': '['}
        

        stack = []

        for i in range(len(s)):
            if s[i] in all_brackets.values():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elif stack[-1] != all_brackets.get(s[i]):
                    return False
                else:
                    stack.pop()
                
        
        if not stack:
            return True
        else:
            return False
        

