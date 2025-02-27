def circle_area():
    r = float(input("Nhập bán kính hình tròn: "))
    return 3.14159 * r * r

def rectangle_area():
    length = float(input("Nhập chiều dài hình chữ nhật: "))
    width = float(input("Nhập chiều rộng hình chữ nhật: "))
    return length * width

def triangle_area():
    base = float(input("Nhập đáy tam giác: "))
    height = float(input("Nhập chiều cao tam giác: "))
    return 0.5 * base * height

def square_area():
    side = float(input("Nhập cạnh hình vuông: "))
    return side * side

def rhombus_area():
    diagonal1 = float(input("Nhập đường chéo thứ nhất của hình thoi: "))
    diagonal2 = float(input("Nhập đường chéo thứ hai của hình thoi: "))
    return (diagonal1 * diagonal2) / 2

def parallelogram_area():
    base = float(input("Nhập đáy hình bình hành: "))
    height = float(input("Nhập chiều cao hình bình hành: "))
    return base * height