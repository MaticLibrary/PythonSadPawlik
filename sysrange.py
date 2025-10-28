def my_range(*args):
    if len(args) < 1 or len(args) > 3:
        return []
    if len(args) == 1:
        start, stop, step = 0.0, args[0], 1.0
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1.0
    else:
        start, stop, step = args

    if step == 0.0:
        return []

    result = []
    current = start

    if step > 0:
        while current < stop:
            result.append(current)
            current += step
    else:
        while current > stop:
            result.append(current)
            current += step

    return result


def main():
    print(my_range(1.1, 2.2, 0.5))
    print(my_range(1.1, 2.1, 0.5))
    print(my_range(1.1, 2.2))
    print(my_range(2.2))
    print(my_range(2.2, 0.1, -0.5))
    print(my_range(1.1, 2.2, 0.0))
    print(my_range(1.1, 2.2, 0.5, 0.1))

main()
