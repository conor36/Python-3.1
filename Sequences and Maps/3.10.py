def get_counts_dict(wlist):
    lengths = [len(word) for word in wlist]
    return {number : lengths.count(number) for number in lengths}