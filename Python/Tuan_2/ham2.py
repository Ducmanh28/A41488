def Schunhat(a,b):
    return(a*b)

def Binhphuong(a):
    return(a*a)

def Giaithua(a):
    result = 1
    for i in range(1,a+1,1):
        result *= i
    return result
        
print("Dien tich la: ",Schunhat(5,8))
print("Binh phuong la: ",Binhphuong(5))
print("Giai thua la: ",Giaithua(5))