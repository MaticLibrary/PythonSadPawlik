def my_range(*args):
    if len(args) < 1 or len(args) > 3:
        yield None
        return
    if len(args) == 1:
        start, stop, step = 0.0, args[0], 1.0
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1.0
    else:
        start, stop, step = args

    if step == 0.0:
        yield None
        return

    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    else:
        while current > stop:
            yield current
            current += step


def main():
    for x in my_range(1.1, 2.2, 0.5):
        print(x)
    for x in my_range(2.2, 0.1, -0.5):
        print(x)

main()
