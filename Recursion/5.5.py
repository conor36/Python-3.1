class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

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

    def recursive_count(self, ptr):
        if ptr == None:
            return 0
        return 1 + self.recursive_count(ptr.next)

    def count(self):
        return self.recursive_count(self.head)

    def rec_count_even(self, ptr):
        if ptr == None:
            return 0

        if int(ptr.item) % 2:
            return self.rec_count_even(ptr.next)
        else:
            return 1 + self.rec_count_even(ptr.next)

    def count_even(self):
        return self.rec_count_even(self.head)

    def rec_is_present(self, ptr, arg):
        if ptr == None:
            return False

        if ptr.item == arg:
            return True
        else:
            return self.rec_is_present(ptr.next, arg)

    def is_present(self, arg):
        return self.rec_is_present(self.head, arg)

    def rec_largest(self, ptr, curr_max = None):
        if ptr == None:
            return curr_max

        if curr_max == None:
            curr_max = self.head.item
        elif ptr.item > curr_max:
            curr_max = ptr.item
        return self.rec_largest(ptr.next, curr_max)

    def largest(self):
        return self.rec_largest(self.head)

    def rec_duplicates(self, ptr):
        try:
            if ptr.item == ptr.next.item:
                return True
            else:
                return self.rec_duplicates(ptr.next)
        except:
            return False

    def duplicates(self):
        return self.rec_duplicates(self.head)