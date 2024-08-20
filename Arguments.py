def positional_and_key_args(x, y, /, *, z, w):
    """
    Write a function with positional and keyword arguments.
    Input: func(5, 10, z=15, w=20) Expected Output: 5, 10, 15, 20
    """
    return x + y + z + w


print(positional_and_key_args(1, 2, z=3, w=4))  # 1

