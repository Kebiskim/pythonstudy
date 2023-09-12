class Calculator:
    @staticmethod
    def plus(a, b):
        return a+b
    @staticmethod
    def minus(a, b):
        return a-b
    # 스태틱 메서드를 쓸 수 있음!
    @staticmethod
    def multiply(a, b):
        return a*b
    @staticmethod
    def divide(a, b):
        return a/b

if __name__ == '__main__':
    print("{0} + {1} = {2}".format(7, 4, Calculator.plus(7,4)))
    print("{0} - {1} = {2}".format(7, 4, Calculator.minus(7,4)))
    print("{0} * {1} = {2}".format(7, 4, Calculator.multiply(7,4)))
    print("{0} / {1} = {2}".format(7, 4, Calculator.divide(7,4)))