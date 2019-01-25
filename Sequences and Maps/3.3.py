def get_evenodd_list():
    num = int(input())
    odd = []
    even = []
    while num != -1:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)
        num = int(input()) 
    return odd, even