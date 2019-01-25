import sys

def main():
    students = open(sys.argv[1], "r")
    delinquents = open(sys.argv[2], "r")
    names = [line.strip() for line in students]
    double = []
    for line in delinquents:
        delname = line.strip()
        if delname in names:
            double.append(delname)
    for i in range(len(double)):
        print(str(i+1) + ".", sorted(double)[i])
    students.close()
    delinquents.close()

if __name__ == "__main__":
    main()