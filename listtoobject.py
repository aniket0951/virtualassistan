class MyClass:
    def __init__(self, val):
        self.val = val


ls = [1, 2, 3]
objs = {val: MyClass(val) for val in ls}
objs = [MyClass(val) for val in ls]
print(objs)

