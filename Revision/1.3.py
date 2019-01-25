import sys

def main(argv):
    print (":" + ":".join(sys.argv[1:]) + ":")


if __name__ == "__main__":
    main(sys.argv[1:])