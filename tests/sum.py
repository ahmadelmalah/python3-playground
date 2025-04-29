def sum(x, y):
    return x + y


def myfunc_error():
    raise ValueError("Exception 123 raised")


def function_uses_external_dependency():
    value = get_value_from_a_remote_server()
    print("value:", value)
    return value


def get_value_from_a_remote_server():
    return 42
