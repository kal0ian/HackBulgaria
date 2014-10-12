# generate_numbers.py
import sys
from random import randint


def main():
    filename = sys.argv[1]
    file = open(filename, "w")
    contents = []
    n = int(sys.argv[2])
    for i in range(0, n):
        buf = randint(1, 1000)
        contents.append(str(buf))

    file.write(" ".join(contents))
    file.close()

if __name__ == '__main__':
    main()
