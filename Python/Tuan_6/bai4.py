from tkinter import *
from tkinter import messagebox
import _mysql_connector

root = Tk()
root.title('Duyệt bản ghi')
root.geometry('500x300')

varName = StringVar()
priceName = StringVar()
desName = StringVar()
varGo = StringVar()

Label(root, text='Tên hải sản:').place(x=20, y=20)
txtName = Entry(root, width=50, textvariable=varName).place(x=120, y=20)

Label(root, text='Giá hải sản:').place(x=20, y=60)
txtPrice = Entry(root, width=50, textvariable=priceName).place(x=120, y=60)

Label(root, text='Mô tả:').place(x=20, y=100)
txtDescription = Entry(root, width=50, textvariable=desName).place(x=120, y=100)
# List chứa danh sách bản ghi
listSeaFood = []

# Biến toàn cục chứa bản ghi hiện tại
currentIndex = 0

# Hàm hiển thị bản ghi đầu tiên
def displayFirst():
    global currentIndex
    currentIndex = 0
    selectedRow = listSeaFood[currentIndex]
    varName.set(selectedRow[0])
    priceName.set(selectedRow[1])
    desName.set(selectedRow[2])
    print('currentIndex = ', currentIndex)

# Hàm hiển thị bản ghi kế tiếp
def displayNext():
    global currentIndex
    if currentIndex == len(listSeaFood) - 1:
        messagebox.showinfo("Thông báo lỗi!", "Bạn đang duyệt bản ghi cuối cùng rồi!")
        return
    else:
        currentIndex = currentIndex + 1
        selectedRow = listSeaFood[currentIndex]
        varName.set(selectedRow[0])
        priceName.set(selectedRow[1])
        desName.set(selectedRow[2])
        # print('currentIndex = ', currentIndex)
# Hàm hiển thị bản ghi trước đó
def displayPrevious():
    global currentIndex
    if currentIndex == 0:
        messagebox.showinfo("Thông báo lỗi!", "Bạn đang duyệt bản ghi đầu tiên rồi!")
        return
    else:
        currentIndex = currentIndex - 1
        selectedRow = listSeaFood[currentIndex]
        varName.set(selectedRow[0])
        priceName.set(selectedRow[1])
        desName.set(selectedRow[2])
        # print('currentIndex = ', currentIndex)

# Hàm hiển thị bản ghi cuối cùng
def displayLast():
    global currentIndex
    currentIndex = len(listSeaFood) - 1
    selectedRow = listSeaFood[currentIndex]
    varName.set(selectedRow[0])
    priceName.set(selectedRow[1])
    desName.set(selectedRow[2])
    # print('currentIndex = ', currentIndex)

# Hàm hiển thị bản ghi theo form nhập
def displayAbsolute():
    index = int(varGo.get())
    global currentIndex
    currentIndex = index - 1
    selectedRow = listSeaFood[currentIndex]
    varName.set(selectedRow[0])
    priceName.set(selectedRow[1])
    desName.set(selectedRow[2])

db = mysql.connect("localhost","root","","quanlyhaisan")
cursor = db.cursor()
cursor.execute("SELECT ten,gia,mota FROM haisan")

for ten,gia,mota in cursor.fetchall():
    row = [ten,gia,mota]
    listSeaFood.append(row)
    
btnFirst = Button(root,text="Đầu tiên",command=displayFirst).place(x=60,y=140)
btnPrevious = Button(root,text="Trước",command=displayPrevious).place(x=120,y=140)
btnNext = Button(root,text="Tiếp",command=displayNext).place(x=170,y=140)
btnLast = Button(root,text="Cuối",command=displayLast).place(x=210,y=140)
btnExit = Button(root,text="Thoát",command=root.destroy).place(x=280,y=140)

Label(root, text="Chọn bản ghi:").place(x=60,y=200)
txtGo = Entry(root, width=10,textvariable=varGo).place(x=150,y=200)
btnGo = Button(root,text="Chọn",command=displayAbsolute).place(x=200,y=200)

root.mainloop()