class Stack:

   def __init__(self):
      self.stack = []
      self.top = 0

   def is_empty(self):
      return self.top == 0

   def push(self, item):
      if self.top < len(self.stack):
         self.stack[self.top] = item
      else:
         self.stack.append(item)

      self.top += 1

   def pop(self):
      if self.is_empty():
         return None
      else:
         self.top -= 1
         return self.stack[self.top]

def reverse_input(stack):
    lst = sys.stdin.readlines()
    for i in lst:
        if i != "\n":
            Stack.push(stack, i.strip())
    while stack.is_empty() == False:
        print(stack.pop())