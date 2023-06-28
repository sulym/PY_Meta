class BoolConversionError(Exception):
    pass


def from_int(value: int) -> None:
    
    if not isinstance(value, int):
        raise TypeError
    elif value == 1:
        return True
    elif value == 0:
        return False
    else:
        raise ValueError
    

def from_str(value: str) -> None:
    if not isinstance(value, str):
        raise TypeError
    elif value in ["True", "T", "1"]:
        return True
    elif value in ["False", "F", "0"]:
        return False
    else:
        raise ValueError
    

def make_bool(value: any) -> bool:
    try:
        try:
            b = from_int(value)
        except TypeError:
            try:
                b = from_str(value)
            except TypeError:
                raise BoolConversionError(
                    f"Cannot convert to the bool {type(value)} type"
                )
    except ValueError:
        raise BoolConversionError(f"Cannot convert to the bool {value} value")
    else:
        return b