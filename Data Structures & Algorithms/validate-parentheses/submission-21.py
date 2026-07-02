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
        # could push opening brackets to a stack
        # when we see a closing bracket, check if it matches the most recent opening
        # bracket, if so, pop the opening bracket from the stack
        # continuing doing so till theres nothing in the stack
        # empty stack means valid string s, else invalid
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
            if bracket not in brackets:
                bracket_stack.append(bracket)
            else: 
                if not bracket_stack:
                    return False
                elif brackets[bracket] != bracket_stack[-1]:
                    return False
                bracket_stack.pop()

        return not bracket_stack

            