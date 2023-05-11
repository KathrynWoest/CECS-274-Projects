import numpy as np
import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator
import re


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def matched_expression(self, s: str) -> bool:
        stack = ArrayStack.ArrayStack()
        for i in s:
            if i == "(":
                stack.push(i)
            elif i == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False
        if stack.n == 0:
            return True
        else:
            return False

    def _build_parse_tree(self, exp: str) -> str:
        if self.matched_expression(exp) == False:
            raise ValueError
        t = BinaryTree.BinaryTree()
        current = t.r = t.Node()
        token = []
        variables = [x for x in re.split('\W+', exp) if x.isalnum()]  # list of variables
        everything_else = re.split('\w+', exp)  # list of tokens btw each variable/at the ends of the string
        for k in range(len(everything_else)):  # for the length of the token list
            for j in everything_else[k]:
                token.append(j)
            if k in range(len(variables)):  # if not at end of variable list, add the variable
                token.append(variables[k])
        for i in token:
            if i == "(":
                current.insert_left(t.Node())
                current = current.left
            elif i == "+" or i == "-" or i == "/" or i == "*":
                current.set_val(i)
                current.set_key(i)
                current.insert_right(t.Node())
                current = current.right
            elif i != ")":
                current.set_key(i)
                current.set_val(self.dict.find(i))
                current = current.parent
            else:
                current = current.parent
        return t

    def _evaluate(self, u):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if u.left != None and u.right != None:
            op2 = op[u.k]
            return op2(self._evaluate(u.left), self._evaluate(u.right))
        elif u.left == None and u.right == None:
            if u.k == None:
                raise ValueError  # missing right operand
            elif u.v != None:
                return u.v
            else:
                raise ValueError  # variable is not defined
        else:
            raise ValueError  # missing at least one operand and maybe an operator, depending on situation

    def evaluate(self, exp):
        parseTree = self._build_parse_tree(exp)
        return self._evaluate(parseTree.r)

    def print_expression(self, expr):
        variables = [x for x in re.split('\W+', expr) if x.isalnum()]  # list of variables
        everything_else = re.split('\w+', expr)  # list of tokens btw each variable/at the ends of the string
        for i in range(len(variables)):
            found = self.dict.find(variables[i])
            if found != None:
                variables[i] = found
        new_expr = ""
        for k in range(len(everything_else)):  # for the length of the token list
            new_expr += str(everything_else[k])
            if k in range(len(variables)):  # if not at end of variable list, add the variable
                new_expr += str(variables[k])
        print(new_expr)
