from test_framework import generic_test


def power(x, y):
    if y == 0:
        return 1
    pwr, result = 1, x
    while (pwr << 1) < abs(y):
        result *= result
        pwr <<= 1
    if pwr < abs(y):
        result *= x
    if y < 0:
        result = 1 / result
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
