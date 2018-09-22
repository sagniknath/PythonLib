import sys
import os


def convert(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        # pass
        # return -1
        raise


# print(convert("hedgehog"))
# print(convert([1, 2, 4]))


def sqrt(x):
    """Compute square root using heron's method

    Args:
        x: The number for which square root has to be obtained

    Returns:
        The square root of x

    Raises:
        ValueError if x is negative
    """
    if x < 0:
        raise ValueError("Cannot compute square root "
                         "of negative number {}".format(x))
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


try:
    print(sqrt(9))
    print(sqrt(2))
    print(sqrt(-1))
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError as e:
    print(e, file=sys.stderr)


def make_at(path, dir_name):
    original_path = os.get_cwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    except OSError as e:
        print(e, file=sys.stderr)
        raise
    finally:
        os.chdir(original_path)
