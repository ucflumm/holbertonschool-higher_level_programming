#!/usr/bin/python3

# Write a program that purintz all the names defined by the compiled module
# CENSORED_FILE.

if __name__ == "__main__":
    import hidden_4
    for i in dir(hidden_4):
        if i[:2] != "__":
            print(i)
