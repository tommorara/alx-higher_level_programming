#!/usr/bin/python3
"""program that prints all the names defined by the compiled module"""
if __name__ == "__main__":
    import hidden_4

    _name = dir(hidden_4)
    for i in _name:
        if i[:2] != "__":
            print(i)
