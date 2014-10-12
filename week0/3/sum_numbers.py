import sys


def main():
    sum=0
    filename = sys.argv[1]
    file = open(filename, "r")
    content=file.read()
    file.close()
    content=content.split(" ")
    for i in range(0,len(content)):
        buf=content[i]
        buf=int(buf)
        sum+=buf
    print(sum)

if __name__ == '__main__':
    main()
