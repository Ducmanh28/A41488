from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

root = tk.Tk()
root.title("Register Form")
root.geometry("500x600")
root.config(bg="#CCCCCC")

font_label = ("Times",12,"bold")
font_entry = ("Arial",10)

lbl_header = tk.Label(root, text="Register Form",bg="blue",fg="white",
                      font=("Arial",16,"bold"),width=20)
lbl_header.place(x=25,y=40)

tk.Label(root, text="Full Name:", bg="#CCCCCC",font=font_label).place(x=80,y=120)
entry_name = tk.Entry(root,width=30, font=font_entry)
entry_name.place(x=240,y=120)

tk.Label(root, text="Date of Birth:", bg="#CCCCCC",font=font_label).place(x=80,y=170)
entry_dob = DateEntry(root, width=27, font=font_entry, date_pattern='dd/mm/yyyy')
entry_dob.place(x=240,y=170)

tk.Label(root,text="Email:",bg="#CCCCCC",font=font_label).place(x=80,y=220)
entry_email = tk.Entry(root,width=30,font=font_entry)
entry_email.place(x=240,y=220)

tk.Label(root,text="Course:",bg="#CCCCCC",font=font_label).place(x=80,y=270)
combo_course = ttk.Combobox(root, width=27,font=font_entry,
                            values=["Python","Java","C++"])
combo_course.set("Select Course")
combo_course.place(x=240,y=270)

tk.Label(root,text="Gender:",bg="#CCCCCC",font=font_label).place(x=80,y=320)
var_gender = tk.IntVar()
rd_male = tk.Radiobutton(root,text="Male",variable=var_gender,value=1,bg="#CCCCCC",font=font_entry)
rd_male.place(x=240,y=320)
rd_female = tk.Radiobutton(root,text="Female",variable=var_gender,value=2,bg="#CCCCCC",font=font_entry)
rd_female.place(x=320,y=320)

btn_sumbit = tk.Button(root,text="Sumbit",width=15,bg="green",fg="white",font=font_entry)
btn_sumbit.place(x=180,y=400)

def submit_form():
    # Lấy dữ liệu từ các ô nhập
    name = entry_name.get()
    email = entry_email.get()
    dob = entry_dob.get()
    gender = var_gender.get() # 1=Male, 2=Female, 0=Chưa chọn
    course = combo_course.get()

    # --- VALIDATE: Kiểm tra dữ liệu bắt buộc ---
    # Nếu bất kỳ trường nào bị rỗng
    if name == "" or email == "" or dob == "" or course == "Select course":
        messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
        return # Dừng hàm, không chạy tiếp
    
    # Kiểm tra riêng trường Gender (Radio button)
    if gender == 0:
        messagebox.showerror("Lỗi", "Vui lòng chọn giới tính!")
        return

    # Nếu tất cả đều đúng -> Thông báo thành công
    messagebox.showinfo("Thành công", f"Đã đăng ký!\n\nHọc viên: {name}\nKhóa học: {course}")

# --- 2. Hàm xử lý khi bấm nút Cancel ---
def clear_form():
    # Xóa nội dung các ô
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    
    # Đặt lại giá trị mặc định
    entry_dob.set_date(None)       # Xóa ngày
    combo_course.set("Select course") # Đặt lại combobox
    var_gender.set(0)              # Bỏ chọn giới tính

root.mainloop()