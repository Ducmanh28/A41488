from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title("buchalacha")
ws.config(bg='#0B5A81')

f=('Times',14)
var =StringVar()
var.set('male')
countries=[]
variable =StringVar()

world=open('Python/Tuan_6/countries.txt','r')
for country in world:
    country = country.rstrip('\n')
    countries.append(country)
right_frame=Frame(
    ws,bd=2,bg='#CCCCCC',
    relief=SOLID,padx=10,pady=10

)
Label(right_frame,text="Ho ten:",bg='#CCCCCC',font=f).grid(row=0, column=0,sticky=W,pady=10)

Label(right_frame,text="Email:",bg='#CCCCCC',font=f).grid(row=1, column=0,sticky=W,pady=10)
Label(right_frame,text="Dien thoai:",bg='#CCCCCC',font=f).grid(row=2, column=0,sticky=W,pady=10)
Label(right_frame,text="Chon gioi tinh:",bg='#CCCCCC',font=f).grid(row=3, column=0,sticky=W,pady=10)
Label(right_frame,text="Chon quoc gia:",bg='#CCCCCC',font=f).grid(row=4, column=0,sticky=W,pady=10)
Label(right_frame,text="Password:",bg='#CCCCCC',font=f).grid(row=5, column=0,sticky=W,pady=10)
Label(right_frame,text="Re-Enter Password:",bg='#CCCCCC',font=f).grid(row=6, column=0,sticky=W,pady=10)

gender_frame=LabelFrame(
    right_frame,bg='#CCCCCC',padx=10,pady=10,
)
txtName=Entry(right_frame,font=f)
txtEmail=Entry(right_frame,font=f)
txtMobile=Entry(right_frame,font=f)

male_rb=Radiobutton(gender_frame,
                    text='Nam',bg='#CCCCCC',
                    variable=var,value='male',font=('Times',10),)

female_rb=Radiobutton(gender_frame,
                    text='Nu',bg='#CCCCCC',
                    variable=var,value='female',font=('Times',10),)

others_rb=Radiobutton(gender_frame,
                    text='Khac',bg='#CCCCCC',
                    variable=var,value='others',font=('Times',10),)
register_country=OptionMenu(
    right_frame,variable,*countries
)
register_country.config(
    width=15,font=('Times',12)
)
txtPassword=Entry(
    right_frame,font=f,show='*'
)
txtConfirmPassword=Entry(
    right_frame,font=f,show='*'
)

def validateform():
    if txtName.get()=="":
        messagebox.showinfo("Thong bao loi")
        txtName.focus_set ()
        return
    if txtEmail.get() == "":
        messagebox.showinfo("Thông báo lỗi !", "Bạn cần nhập địa chỉ email !")
        txtEmail.focus_set()
        return

    if txtMobile.get() == "":
        messagebox.showinfo("Thông báo lỗi !", "Bạn cần nhập số điện thoại !")
        txtMobile.focus_set()
        return

    if var.get() == "":
        messagebox.showinfo("Thông báo lỗi !", "Bạn cần chọn giới tính !")
        #txtName.focus_set()
        return

    if variable.get() == "":
        messagebox.showinfo("Thông báo lỗi !", "Bạn cần chọn quốc gia !")
        # txtName.focus_set()
        return

    if txtPassword.get() == "":
        messagebox.showinfo("Thông báo lỗi !", "Bạn cần nhập mật khẩu !")
        txtPassword.focus_set()
        return

    if txtConfirmPassword.get() == "":
        messagebox.showinfo("Thông báo lỗi !", "Bạn cần nhập xác nhận mật khẩu !")
        txtConfirmPassword.focus_set()
        return
    if (txtPassword.get() != txtConfirmPassword.get()):
                    
        messagebox.showinfo("Thông báo lỗi !", "Mật khẩu và xác nhận mật khẩu không khớp !")
                        
        txtPassword.focus_set()
                    
    return
                    
    
register_btn = Button(
    right_frame, width=15, text='Register',
    font=f, relief=SOLID, cursor='hand2', command=validateform)
txtName.grid(row=0, column=1, pady=10, padx=20)
txtEmail.grid(row=1, column=1, pady=10, padx=20)
txtMobile.grid(row=2, column=1, pady=10, padx=20)
register_country.grid(row=4, column=1, pady=10, padx=20)
txtConfirmPassword.grid(row=6, column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.pack()

gender_frame.grid(row=3, column=1, pady=10, padx=20)
male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)
others_rb.pack(expand=True, side=LEFT)

ws.mainloop()