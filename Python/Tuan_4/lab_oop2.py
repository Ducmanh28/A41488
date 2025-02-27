class Calculator:
    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def divide(self, a, b):
        if b == 0:
            return "Lỗi: Không thể chia cho 0"
        return a / b

    def multiple(self, a, b):
        return a * b

    def factorial(self, n):
        if n < 0:
            return "Lỗi: Không thể tính giai thừa của số âm"
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

calc = Calculator()

print(f"{a} + {b} = {calc.add(a, b)}")
print(f"{a} - {b} = {calc.minus(a, b)}")
print(f"{a} * {b} = {calc.multiple(a, b)}")
print(f"{a} / {b} = {calc.divide(a, b)}")

n = int(input("Nhập số để tính giai thừa: "))
print(f"{n}! = {calc.factorial(n)}")
