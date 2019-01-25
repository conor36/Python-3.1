def insertion_sort(lst):
    comparisons = 0
    moves = 0 
    
    for todo in range(1, len(lst)):
        tobeinserted = lst[todo]
        i = todo
        while i > 0 and tobeinserted < lst[i-1]:
            lst[i] = lst[i-1]
        
            moves += 1
            comparisons += 1
            i -= 1
        
        lst[i] = tobeinserted
        if i > 0:
            comparisons += 1
        
        
    return  (comparisons , moves + ((len(lst) - 1) * 2))