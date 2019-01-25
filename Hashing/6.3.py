from LinkedList import LinkedList

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)

    def min_max_bucket_length(self):
        maxm = None
        minm = None
        for x in self.table:
            if x != None and len(x) != 0:
                if minm == None or len(x) < minm:
                    minm = len(x)
                if maxm == None or len(x) > maxm:
                    maxm = len(x)
        return (minm,maxm)