class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.height = 0
    
    def print_dummy_stack(self, stack = 'Original Stack'):
        if(not self.top):
            print(f'Their are no elements in the {stack}')
        else:
            print(f'The elements in the {stack} are ')
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
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp.value
    
    def sorting(self):
        if(not self.top):
            print('No elements to sort in the stack')
        elif(self.top.next == None):
            print(self.top.value)
        else:
            dummy_stack = Stack()
            while(self.top != None):
                val_ori = self.pop()
                if(not dummy_stack.top):
                    dummy_stack.push(val_ori)
                else:
                    if(dummy_stack.top.value >= val_ori):
                        dummy_stack.push(val_ori)
                    else:
                        while(dummy_stack.top != None and dummy_stack.top.value < val_ori):
                            val_dum = dummy_stack.pop()
                            self.push(val_dum)
                        dummy_stack.push(val_ori)
                dummy_stack.height += 1
            dummy_stack.print_dummy_stack('Dummy Stack')


sk = Stack()
ran = int(input('Enter the count to push the values into the stack : '))
print('Enter the values to push : ')
for i in range(ran):
    sk.push(int(input()))
print('\nAfter sorting the original stack, elements are')
sk.sorting()
print()
sk.print_dummy_stack()