from typing import Callable, Any
from inspect import signature


def strict(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        sig = signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        for param_name, param_value in bound_args.arguments.items():
            expected_type = func.__annotations__.get(param_name)
            if expected_type is not None and not isinstance(param_value, expected_type):
                raise TypeError(f"Аргумент '{param_name}' должен быть типа {expected_type.__name__}, "
                              f", но получил {type(param_value).__name__}")

        result = func(*args, **kwargs)
        return_type = func.__annotations__.get('return')
        if return_type is not None and not isinstance(result, return_type):
            raise TypeError(f"Return value must be of type {return_type.__name__}, "
                          f"got {type(result).__name__} instead")
        return result

    return wrapper 