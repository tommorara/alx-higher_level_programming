#!/usr/bin/python3
"""program that prints the result of the addition of all arguments"""
if __name__ == "__main__":
    import sys

    overall = 0
    for q in range(len(sys.argv) - 1):
        overall += int(sys.argv[q + 1])
    print("{}".format(overall))
