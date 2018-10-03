from test_framework import generic_test


def power(x, y):
    if y == 0:
        return 1
    pwr, result = y, 1.0
    if pwr < 0:
        pwr, x = -pwr, 1.0 / x
    while pwr:
        if pwr & 1:
            result *= x
        x *= x
        pwr >>= 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
