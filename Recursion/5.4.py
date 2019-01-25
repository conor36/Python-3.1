class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these are methods "A method is a function that is stored as a class attribute"
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None

    def count(self):
        return r_count(self.head)

    def count_even(self):
        return r_count_even(self.head)

    def is_present(self, item):
        return r_is_present(self.head, item)

    def largest(self):
        return r_largest(self.head)

    def duplicates(self):
        return r_duplicates(self.head)

def r_count(ptr):
    if ptr == None:
        return 0
    else:
        return r_count(ptr.next) + 1

def r_count_even(ptr):
    if ptr == None:
        return 0
    elif int(ptr.item) % 2 == 0:
        return r_count_even(ptr.next) + 1
    else:
        return r_count_even(ptr.next)

def r_is_present(ptr, item):
    if ptr == None:
        return False
    elif ptr.item == item:
        return True
    else:
        return r_is_present(ptr.next, item)

def r_largest(ptr, largest = -100000000):
    if ptr == None:
        return largest
    elif int(ptr.item) > largest:
        largest = int(ptr.item)
        return r_largest(ptr.next, largest)
    else:
        return r_largest(ptr.next, largest)

def r_duplicates(ptr):
    if ptr == None and ptr.next == None:
        return False
    elif ptr.item == ptr.next.item:
        return True
    else:
        return r_duplicates(ptr.next)