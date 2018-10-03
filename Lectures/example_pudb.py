import pudb

def main():
    a = 5
    b = 6
    c = a * b
    pudb.set_trace()
    print_me(c)
    return c

def print_me(c):
    """print some stuff

    :param c: value to print
    """

    print(c)

if __name__ == "__main__":
    main()
