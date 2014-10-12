import sys


def main():
    count = 0
    if sys.argv[1] == "chars":
        filename = sys.argv[2]
        file = open(filename, "r")
        content = file.read()
        for i in content:
            count += 1
        print(count)
    elif sys.argv[1] == "words":
        filename = sys.argv[2]
        file = open(filename, "r")
        content = file.read()
        content = content.split(" ")
        print(len(content))
    elif sys.argv[1] == "lines":
        filename = sys.argv[2]
        file = open(filename, "r")
        content = file.read()
        content = content.split("\n")
        print(len(content))
    file.close()

if __name__ == '__main__':
    main()
