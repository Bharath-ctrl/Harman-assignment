def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return (a / b)


if __name__ == "__main__":
    a = int(input("1 num "))
    b = int(input("2 num "))

    print(add(a, b))
    print(sub(a, b))
    print(mul(a, b))
    print(div(a, b))
