import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write
    def reversed_write(text):
        a = 1 / 0
        original_write(text[::-1])
    sys.stdout.write = reversed_write

    try:
        yield "Job"
    except ZeroDivisionError as e:
        e.args = ("please don't divide by zero",)
    finally:
        sys.stdout.write = original_write
        _, ev, _ = sys.exc_info()
        print(ev.args)


with looking_glass() as what:
    print("Alice, Kitty and Snowdrop")
    print(what)

print('asdfasdf')
