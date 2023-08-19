class Testmethod:
    @staticmethod
    def sum(a,b):
        return a + b

    @staticmethod
    def multiply(*args):
        res = 1
        for num in numbers:
            res *= num
        return res

    @classmethod
    def calculate(cls,*args):
        if len(numbers) >= 2:
            return cls.sum(numbers[0],numbers[1]),cls.multiply(*numbers[2:])

numbers = [1,2,3,4,5]
result = Testmethod.calculate(*numbers)
print(result)