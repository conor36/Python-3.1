def set_intersection(first , second):
    return first.intersection(second)

def set_stuff(set1, set2):
    return (set1.union(set2) ,set1.issubset(set2) , set1.issuperset(set2))

def unique_list(a):
    return list(set(a))