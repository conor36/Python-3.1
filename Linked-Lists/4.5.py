def is_empty(self):
        return self.head == None

def even_count(self):
    count = 0
    ptr = self.head
    while ptr != None:
        if ptr.item % 2 == 0:
            count += 1
        ptr = ptr.next
    return count