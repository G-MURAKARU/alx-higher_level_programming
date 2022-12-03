#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    funcs = [func for func in dir(hidden_4) if func[:2] not in "__"]
    for func in funcs:
        print(func)
