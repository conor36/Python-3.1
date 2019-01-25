def insertion_sort(lst):
    comparisons = 0
    moves = 0 
    
    if len(lst) == 0:
        return


    min_index = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
        comparisons += 1

    lst[0], lst[min_index] = lst[min_index], lst[0]
    moves += 1

    for todo in range(2, len(lst)):
        store = lst[todo]
        i = todo
        
        while store < lst[i-1]: 
            lst[i] = lst[i-1] 
            
            moves += 1
            comparisons += 1
            i -= 1
        
        lst[i] = store  
        
        if i > 0:
            comparisons += 1
            
    return  (comparisons , moves + ((len(lst) - 1) * 2))
