import sys

def main():
    a = sys.argv[1]
    l = len(a)
    word = [i for i in a]

    if l % 2 == 0:
        half = int(len(a)/2)
        print("".join(word[half:]))

    else:
        odd = [word[0], word[l-1]]
        print ("".join(odd))

if __name__ == "__main__":
    main()