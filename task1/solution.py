def check_annotation(f):
    def wrapper(*args, **kwargs):
        annotations = f.__annotations__

        for i, (arg, expected_type) in enumerate(zip(args, annotations.values())):
            if not isinstance(arg, expected_type):
                raise TypeError(f"передан аргумент не правильного типа")
        
        for key, value in kwargs.items():
            expected_type = annotations.get(key)
            if expected_type is not None and not isinstance(value, expected_type):
                raise TypeError(f"передан аргумент не правильного типа")
        
        return f(*args, **kwargs)
    return wrapper
