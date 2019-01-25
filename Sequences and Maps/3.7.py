numlst = []
print("Enter numbers (-1 to end): ", end="")
num = int(input())
while num != -1:
    if num in numlst:
        print(str(num) + " ", end="")
    numlst.append(num)
    num = int(input())
print()