import sys


def main():
    contents = []
    for i in range(1, len(sys.argv)):
        filename = sys.argv[i]
        file = open(filename, "r")
        contents.append(file.read())
        file.close()
    file = open("MEGATRON", "a")
    file.write("\n".join(contents))
    file.write("\n")


if __name__ == '__main__':
    main()
