def co(a, b):
    return a + b 

# if result != expected:
#     raise Exception(f"{result} not equal {expected}")
def test_add_too_numbers():
    
    assert co(7,8) == 14

if __name__ == '__main__':
    test_add_too_numbers()

print(__name__)