class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += " " + ptr.item
            ptr = ptr.next

        return tmp_str

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            return item

    def is_empty(self):
        return self.head == None

    def count(self):
        count = 0
        point = self.head
        while point != None:
            count += 1
            point = point.next

        return count

    def contains(self , arg):
        point = self.head
        while point != None:
            if point.item == arg:
                return True
            point = point.next
        return False

    def after(self , arg):
        point = self.head
        while point != None:
            if point.item == arg:
                return point.next.item
            point = point.next

    def before(self , arg):
        point = self.head
        prev = None
        while point != None:
            if point.item == arg:
                return prev
            prev = point.item
            point = point.next

    def append(self, arg):
        ptr = self.head
        previous = Node
        if self.head == None:
            self.add(arg)
        while ptr != None:
            previous = ptr
            ptr = ptr.next
        previous.next = Node(arg, None)

    def rotate(self):
        self.append(self.head.item)
        self.remove()