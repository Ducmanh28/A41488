class NhanVien():
    def hienthi(self):
        print("Chao mung cong ty!")
    def hienthichitiet(self,hoten,luong):
        print("Ho ten la: " + str(hoten) + ". Luong la: " + str(luong))

nv1 = NhanVien()
nv1.hienthi()
nv1.hienthichitiet("Duc Manh",5000000)

class Khachhang():
    hoten=""
    tuoi = 0
    diachi = ""
    
    def __init__(self,hoten,tuoi,diachi):
        self.hoten = hoten
        self.tuoi = tuoi
        self.diachi = diachi
        
    def mota(self):
        print("Ho ten: "+ self.hoten)
        print("Tuoi: "+ str(self.tuoi))
        print("Dia chi: " + self.diachi)
        
obj = Khachhang("Diem My",35,"Ha Noi")
obj.mota()

print("khachhang.doc = " + str(Khachhang.__doc__))
print("khachhang.dic = " + str(Khachhang.__dict__))
print("khachhang.module = " + str(Khachhang.__module__))
print("khachhang.name = " + str(Khachhang.__name__))
print("khachhang.base = " + str(Khachhang.__base__))

