def sum_to_k(lst, k):
    first = 0
    last = len(lst) - 1
    while first < last:
        if lst[first] + lst[last] == k:
            return True
        
        elif lst[first] + lst[last] < k:
            first = first + 1
            
        else:
            last = last - 1
            
    return False