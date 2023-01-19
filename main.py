class DateCalendar:
    def __init__(self):
        pass

    def __call__(self, function):
        print("call")

        def wrapper(*args, **kwargs):
            print('in function', f"{args = }")
            return function(*args, **kwargs)
        return wrapper

@DateCalendar()
def f(name):
    print(f"hello, {name}")

f("anton")