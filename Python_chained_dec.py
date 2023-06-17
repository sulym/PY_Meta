def chained(functions: list) -> any:
    def combined(*args, **kwargs) -> int:
        result = None
        for function in functions:
            if result is None:
                result = function(*args, **kwargs)
            else:
                result = function(result)
        return result
    return combined


### m ###

def chained(functions: list):
    def chain(input_arg):
        for f in functions:
            input_arg = f(input_arg)
        return input_arg
    return chain
