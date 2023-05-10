class Cycle:
    
    def __init__(self, ls: list) -> None:
        self.ls = ls

    def __iter__(self):
        self.cur_elment = 0
        return self
    
    def __next__(self):
        if len(self.ls) == 0:
            raise StopIteration
        result = self.ls[self.cur_elment]
        self.cur_elment += 1
        self.cur_elment %= len(self.ls)
        return result

lsss = [0, 1, 2, 3]
each = Cycle(lsss)

iterator = iter(each)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))