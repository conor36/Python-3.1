def get_sliced_lists(numlist):
    exct_last = numlist[:-1]
    exct_firstlast = numlist[1:-1]
    exct_firstlast2 = numlist[1:-1]
    reverse = numlist[::-1]
    return [exct_last, exct_firstlast, exct_firstlast2, reverse]