def insertion_sort(lst):
    swaps = 0
    comparisons = 0
    
    for todo in range(1, len(lst)):
        i = todo
        while i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            swaps += 1
            i -= 1
            
        if i > 0:
            comparisons += 1
            
        
    
    return (swaps + comparisons, swaps)