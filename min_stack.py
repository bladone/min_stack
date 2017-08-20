#! /usr/bin/env python3

###题目：实现一个栈，带有出栈（pop），入栈（push），取最小元素（getMin）三个方法。要保证这三个方法的时间复杂度都是O（1）。
class Minstack:
    def __init__(self):
        self.stack_main=[0xffffffff]
        self.stack_ind=[0]

    def print_self(self):
        print(self.stack_main)
        print(self.stack_ind)
    
    def push(self,character):
        self.stack_main.append(character)

        if self.stack_main[self.stack_ind[-1]] > character:
            self.stack_ind.append(len(self.stack_main) - 1)            
#        self.print_self()

    def pop(self):
        if len(self.stack_main) - 1 == self.stack_ind[-1]:
            self.stack_ind.pop()
#       self.print_self()        
        return self.stack_main.pop()

    def get_min(self):
        return self.stack_main[self.stack_ind[-1]]

if __name__ == '__main__':
    the_stack=Minstack()
    for i in range(5):    
        input_cha=int(input("please input chara: "))
        the_stack.push(input_cha)
    
    for i in range(5):
        print("The min chara is {:2d}".format(the_stack.get_min()))
        print("pop chara is {:2d}".format(the_stack.pop()))
