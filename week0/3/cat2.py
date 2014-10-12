import sys


def main():
    for i in range(1,len(sys.argv)):
        filename = sys.argv[i]
        file = open(filename, "r")
        print(file.read())
        file.close()

if __name__ == '__main__':
    main()
