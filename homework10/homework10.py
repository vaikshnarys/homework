class Calculate():
    @classmethod
        def sum(cls,a,b):
        return a + b

    @classmethod
    def subtrack(cls,a,b):
        return a - b

    @classmethod
    def multiply(cls,a,b):
        return a * b

    @classmethod
    def devide(cls,a,b):
        return a / b
OPERATOR_NUM = {
    "+" : Calculate.sum,
    "-" : Calculate.subtrack,
    "*" : Calculate.multiply,
    "/" : Calculate.devide,
}
try:
    x = int(input("First num : "))
    y = int(input("Second num : "))
    action = (input("Choose active(+,-,*,/)"))
    result = OPERATOR_NUM[action](x, y)
    print(result)
    if x == 0:
        raise ZeroDivisionError ("first number zero")

except ValueError as exc:
    print(f"Value is not correct: {exc}")
except ZeroDivisionError as exc:
    print(f"Value is not correct: {exc}")
except KeyError as exc:
    print(f"Value is not correct: {exc}")
except EOFError as exc:
    print(f"Value is not correct: {exc}")
