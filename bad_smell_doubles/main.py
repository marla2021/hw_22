class SomeClass:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]

    def sorted(self):
        self.lst.sort()
        return self.lst


if __name__ == "__main__":
    some_inst = SomeClass()
    print(some_inst.sorted())
