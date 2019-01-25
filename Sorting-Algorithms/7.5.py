""" Selection sort algorithm """
def selection_sort(lst):
    comparisons = 0
    swaps = 0
    
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(min_index + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
            comparisons += 1

        if i != min_index:
            lst[i], lst[min_index] = lst[min_index], lst[i]
            swaps += 3
        
            
    return (comparisons, swaps)