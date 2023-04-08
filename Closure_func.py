def one(object):
    def in_on(x):
        return x * object

    return in_on

ver = one(9)
print(ver(3))