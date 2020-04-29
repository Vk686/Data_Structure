from stack import Node
from stack import Stack 

obj = Stack()

expression = input("Enter any expression :")


def balanced_parentheses(expression):
    open_parentheses = "({["
    closed_parentheses = ")}]"

    for brackets in expression:
        if brackets in open_parentheses:
            bracts = Node(brackets)
            obj.push(bracts)
        elif brackets in closed_parentheses:
            obj.pop()

    if obj.is_empty():
        print("Given expression is balanced!!")
    else:
        print("Given expression is Not balanced!!")


balanced_parentheses(expression)