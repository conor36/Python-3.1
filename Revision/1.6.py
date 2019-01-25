def sum_to_k(lst , k):
    for i in range(len(lst)):
       for j in range(i + 1 , len(lst)):
          if lst[i] + lst[j] == k:
             print(lst[i], lst[j])