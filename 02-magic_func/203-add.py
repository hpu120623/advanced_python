class Nums:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        result = Nums(self.x + other.x, self.y + other.y)
        return result

    def __str__(self):
        return f'x:{self.x}, y:{self.y}'


my_num = Nums(10, 20)
other_num = Nums(20, 30)
print(my_num + other_num)
