from LinkedList import LinkedList

def str_hash(s):
   if not isinstance(s, str):
      return hash(s) # not a string => use the normal hash function
   else:
      if len(s) > 0:
         return sum([ord(ch) for ch in s]) 

class HashSet:
   def __init__(self, capacity=10):
      # Create a list to use as the hash table
      self.table = [None] * capacity

   def add(self, item):
      # Find the hash code
      # Define your own hash function and use it instead of the built in hash()
      h = str_hash(item)
      index = h % len(self.table)

      # Check is it empty
      if self.table[index] == None:
         self.table[index] = LinkedList() # Need a new linked list for this entry

      if item not in self.table[index]:
         # Only add it if not already there (this is a set)
         self.table[index].add(item)

   def __str__(self):
      s = ""
      for i in range(len(self.table)):
         s += "table[" + str(i) + "]"
         if self.table[i] != None:
             s += " Head " + str(self.table[i])
         s += "\n"

      return s