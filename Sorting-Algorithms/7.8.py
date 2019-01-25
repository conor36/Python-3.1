comparisons = 0
moves = 0 

def partition(lst, lo, hi):
    global comparisons 
    global moves 
    
    midpoint = (hi + lo) // 2
    lst[lo], lst[midpoint] = lst[midpoint], lst[lo]
    moves += 3
    
    
    part = lo
    while lo < hi:
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
            comparisons += 1
        while lst[hi] > lst[part]: 
            hi -= 1
            comparisons += 1
        
        comparisons += 2
        

        if lo < hi:
            lst[hi], lst[lo] = lst[lo], lst[hi]
            moves += 3

    if lst[part] > lst[hi]: 
        lst[part], lst[hi] = lst[hi], lst[part]
        moves += 3
        
    comparisons += 1
        
        
    return hi

def rec_qsort(lst, lo, hi):
    global comparisons
    global moves
    
    if lo < hi:
        pivot = partition(lst, lo, hi)
        rec_qsort(lst, lo, pivot - 1)
        rec_qsort(lst, pivot + 1, hi)
        

def qsort(lst):
    global comparisons
    global moves
    rec_qsort(lst, 0, len(lst) - 1)
    
    return comparisons, moves
