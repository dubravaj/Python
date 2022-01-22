from functools import wraps

# simple decorator
def custom_decorator(f):
    def wrapper():
        print("Some custom operation before f")
        f()

    return wrapper


# custom decorator for function with arguments
def greet_decorator(f):
    @wraps(f)  # wraps will preserve information about function f
    def wrapper(*args, **kwargs):
        print("Do some processing before greeting...")
        return f(*args, **kwargs)

    return wrapper


# use custom decorator
@custom_decorator
def calculate():
    print("Doing some operation...")


@greet_decorator
def greet_person(name: str) -> str:
    print(f"Hello {name}! Welcome.")
    return print(f"greeted person was: {name}")


# decorator to be used on class instance method
# therefore the wrapper contains reference to instance
def trace_call(name):
    def trace_call_decorator(f):
        @wraps(f)
        def trace_wrapper(self, *args, **kwargs):
            print(f"Processing trace name- {name}")
            f(self, *args, *kwargs)

        return trace_wrapper

    return trace_call_decorator


class Process:
    @trace_call(name="trace-processing")
    def do_processing(self, item_id: int) -> None:
        print(f"Processing item: {item_id}")


if __name__ == "__main__":
    calculate()
    # decorator does not use wraps, so name of function is wrapper inside decorator
    print(calculate.__name__)
    # greet
    greet_person("Peter")
    print(greet_person.__name__)

    processor = Process()
    processor.do_processing(42)
