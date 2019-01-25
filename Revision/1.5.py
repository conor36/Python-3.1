import sys

def main():
    a = [i for i in sys.argv[1]]
    j = 0
    k = 1
    while j <= len(a)-1 and k < len(a):
        word = [a[j], a[k]]
        print ("".join(word))
        k+=1
        j+=1

if __name__ == "__main__":
    main()