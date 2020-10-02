import time


def func(f):
    def wrapper(*args, **kwargs):
        print("\nStarted")
        rv = f(*args, **kwargs)
        print("Ended\n")
        return rv

    return wrapper


@func
def func2(x, y):
    print(x)
    return y


x = func2(5, 6)


def timer(func):
    """
    Timer decorator
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print(f"Time: {total}")

        return rv

    return wrapper


@timer
def test_timer():
    time.sleep(2)


test_timer()
