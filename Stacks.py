class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        if(not self.top):
            print('Their are no elements in the stack to print')
        else:
            curr = self.top
            while(curr):
                print(curr.value)
                curr = curr.next
    
    def push(self, value):
        new_node = Node(value)
        if(not self.top):
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    
    def pop(self):
        if(not self.top):
            print('Their are no elements to pop from the stack')
        else:
            print('The poped element from the stack is ', self.top.value)
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
    
    def peek(self):
        if(not self.top):
            print('Their are no elements to get from the stack to get')
        else:
            print('The peek element present in the stack is ', self.top.value)


sk = Stack(10)
sk.print_stack()
print('After pushing the values the updated stack is ')
sk.push(20)
sk.push(30)
sk.print_stack()
print('Height of the stack is ', sk.height)
sk.pop()
print('After poping the elements in the stack is ')
sk.print_stack()
print('Height of the stack is ', sk.height)
sk.push(30)
sk.push(40)
sk.push(50)
sk.print_stack()
sk.peek()