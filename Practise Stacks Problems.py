class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stacks:
    def __init__(self, value):
        if(value == ')' or value == '()'):
            self.top = None
            self.height = 0
            print('Incorrect use of parenthesis in the initilization step')
        else:
            new_node = Node(value)
            self.top = new_node
            self.stack_list = []
            self.height = 1
    
    def print_stack_list(self):
        if(not self.stack_list):
            print('Their are no elements in the stack list')
        else:
            for i in range(len(self.stack_list) - 1, -1, -1):
                print(self.stack_list[i])
    
    
    def push(self, value):
        self.stack_list.append(value)
    
    def pop(self):
        if(not self.stack_list):
            print('Their are no elements in the stack list')
        else:
            self.stack_list.pop()
    
    def push_parenthesis(self, paren):
        new_node = Node(paren)
        if(paren == '('):
            if(not self.top):
                self.top = new_node
            else:
                new_node.next = self.top
                self.top = new_node
            self.height += 1
        elif(paren == ')'):
            if(not self.top):
                pass
            else:
                temp = self.top
                self.top = self.top.next
                temp.next = None
            self.height -= 1
        else:
            pass
    
    def push_string(self, lett):
        new_node = Node(lett)
        if(not self.top):
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    
    def reverse_string(self):
        if(not self.top):
            print('No string present in the stack')
        else:
            print('After reversing the string ', end = '')
            while(self.top):
                temp = self.top
                self.top = self.top.next
                print(temp.value, end = '')
                temp.next = None



sk1 = Stacks(')')
sk1.push_parenthesis('(')
sk1.push_parenthesis('(')
sk1.push_parenthesis('(')
sk1.push_parenthesis(')')
sk1.push_parenthesis(')')
sk1.push_parenthesis(')')
sk1.push_parenthesis('(')
sk1.push_parenthesis('(')
sk1.push_parenthesis(')')
sk1.push_parenthesis(')')
sk1.push_parenthesis('(')
sk1.push_parenthesis(')')

if(sk1.height == 0):
    print('Order of parenthesis is correct')
else:
    print('Incorrect use of parenthesis')

word = input('Enter a string : ')
sk2 = Stacks(word[0])
for i in range(1, len(word)):
    sk2.push_string(word[i])
sk2.reverse_string()