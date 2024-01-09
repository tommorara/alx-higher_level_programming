#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    len_arg = len(argv) - 1
    str_arg = "argument" if len_arg == 1 else "arguments"
    delim_str = "." if len_arg == 0 else ":"

    print("{} {}{}".format(len_arg, str_arg, delim_str))

    for q in range(1, len_arg + 1):
        print("{}: {}".format(q, argv[q]))
