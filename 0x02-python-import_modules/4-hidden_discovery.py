#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for e in dir(hidden_4):
        if e[0] != '_':
            print(e)
