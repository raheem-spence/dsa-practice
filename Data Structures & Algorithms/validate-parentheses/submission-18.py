class Solution:
    def isValid(self, s: str) -> bool:
        # given: a string s consisting of characters: 
        # '(', ')', '{', '}', '[' and ']'
        # goal: return True if s is a valid string meaning every open
        # bracket is closed by the same type, in the correct order, and
        # every close bracket has a corresponding open bracket of the same type
        # pattern: stack?
        # approach: could use a hash map where key:value pairs are opening and
        # closing brackets of the same type.
        # could push opening brackets to a stack and check if the next bracket
        # is the closing bracket, if so, pop the opening bracket from the stack
        # continuing doing so till theres nothing in the string meaning its s is 
        # valid. If any brackets remain then invalid
        # also, if first bracket is a closing bracket return False

        # example: "("
        # bracket_stack = ['(']

        brackets = {
            ')':'(',
            '}': '{',
            ']': '['
        }

        bracket_stack = []

        for bracket in s:
            if len(bracket_stack) == 0 and bracket in brackets:
                return False
            elif bracket in brackets.values():
                bracket_stack.append(bracket)
            elif brackets[bracket] == bracket_stack[-1]:
                bracket_stack.pop()
            else:
                return False

        if len(bracket_stack) == 0:
            return True
        else: 
            return False

            