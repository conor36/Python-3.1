def detect_loop(self):
        start_ptr = self.head
        try:
            check_ptr = self.head.next
        except:
            return False
        while check_ptr != None:
            if check_ptr.item == start_ptr.item:
                return True
            check_ptr = check_ptr.next
        return False