class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c

def main():
    while True:
        print("\nChọn hình để tính toán:")
        print("1. Hình chữ nhật")
        print("2. Hình vuông")
        print("3. Hình tròn")
        print("4. Hình tam giác")
        print("5. Thoát")
        
        choice = input("Nhập lựa chọn: ")
        
        if choice == '1':
            length = float(input("Nhập chiều dài: "))
            width = float(input("Nhập chiều rộng: "))
            rect = Rectangle(length, width)
            print(f"Diện tích: {rect.area()}, Chu vi: {rect.perimeter()}")
        elif choice == '2':
            side = float(input("Nhập cạnh: "))
            square = Square(side)
            print(f"Diện tích: {square.area()}, Chu vi: {square.perimeter()}")
        elif choice == '3':
            radius = float(input("Nhập bán kính: "))
            circle = Circle(radius)
            print(f"Diện tích: {circle.area()}, Chu vi: {circle.perimeter()}")
        elif choice == '4':
            a = float(input("Nhập cạnh a: "))
            b = float(input("Nhập cạnh b: "))
            c = float(input("Nhập cạnh c: "))
            if a + b > c and a + c > b and b + c > a:
                triangle = Triangle(a, b, c)
                print(f"Diện tích: {triangle.area()}, Chu vi: {triangle.perimeter()}")
            else:
                print("Ba cạnh không hợp lệ để tạo thành tam giác.")
        elif choice == '5':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

if __name__ == "__main__":
    main()