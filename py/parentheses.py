# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

class Solution:
    def checkParentheses(self, _input):
        parentheses = {"[": "]","(": ")","{": "}"}
        _stack = []
        for i in _input:
            if i in parentheses:
                _stack.append(i)
            elif len(_stack) == 0 or parentheses[_stack.pop()] != i:
                return False
        return len(_stack) == 0

if __name__ == "__main__":
    print Solution().checkParentheses("(){}[]()({[]})")
    print Solution().checkParentheses("()[}{{{{(}}}")
