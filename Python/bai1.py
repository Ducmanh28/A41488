from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry 

# --- 1. Hàm xử lý khi bấm nút Submit ---
def submit_form():
    # Lấy dữ liệu từ các ô nhập
    name = entry_name.get()
    email = entry_email.get()
    dob = entry_dob.get()
    gender = var_gender.get() # 1=Male, 2=Female, 0=Chưa chọn
    contact = entry_contact.get()
    course = combo_course.get()

    # --- VALIDATE: Kiểm tra dữ liệu bắt buộc ---
    # Nếu bất kỳ trường nào bị rỗng
    if name == "" or email == "" or dob == "" or contact == "" or course == "Select course":
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
    entry_contact.delete(0, tk.END)
    
    # Đặt lại giá trị mặc định
    entry_dob.set_date(None)       # Xóa ngày
    combo_course.set("Select course") # Đặt lại combobox
    var_gender.set(0)              # Bỏ chọn giới tính

# =============================================
# GIAO DIỆN CHÍNH (GUI)
# =============================================

# Tạo cửa sổ
root = tk.Tk()
root.title("Registration Form")
root.geometry("500x600")
root.configure(bg="grey") # Màu nền xám

# Cấu hình phông chữ chung
font_label = ("Times New Roman", 12, "bold")
font_entry = ("Arial", 10)

# --- TIÊU ĐỀ ---
lbl_header = tk.Label(root, text="Course Registration form", 
                      bg="blue", fg="white", 
                      font=("Times New Roman", 20, "bold"), width=30)
lbl_header.place(x=25, y=40)

# --- CÁC Ô NHẬP LIỆU ---

# 1. Full Name
tk.Label(root, text="Full Name", bg="grey", font=font_label).place(x=80, y=120)
entry_name = tk.Entry(root, width=30, font=font_entry)
entry_name.place(x=240, y=120)

# 2. Email
tk.Label(root, text="Email", bg="grey", font=font_label).place(x=80, y=170)
entry_email = tk.Entry(root, width=30, font=font_entry)
entry_email.place(x=240, y=170)

# 3. DOB (Ngày sinh) - Dùng DateEntry để có mũi tên chọn ngày
tk.Label(root, text="DOB", bg="grey", font=font_label).place(x=80, y=220)
entry_dob = DateEntry(root, width=27, font=font_entry, date_pattern='dd/mm/yyyy')
entry_dob.place(x=240, y=220)

# 4. Gender (Giới tính) - Dùng Radiobutton
tk.Label(root, text="Gender", bg="grey", font=font_label).place(x=80, y=270)
var_gender = tk.IntVar() # Biến để lưu giá trị (1 hoặc 2)
rd_male = tk.Radiobutton(root, text="Male", variable=var_gender, value=1, bg="grey", font=("Arial", 10, "bold"))
rd_male.place(x=240, y=270)
rd_female = tk.Radiobutton(root, text="Female", variable=var_gender, value=2, bg="grey", font=("Arial", 10, "bold"))
rd_female.place(x=320, y=270)

# 5. Contact no.
tk.Label(root, text="Contact no.", bg="grey", font=font_label).place(x=80, y=320)
entry_contact = tk.Entry(root, width=30, font=font_entry)
entry_contact.place(x=240, y=320)

# 6. Select course (Chọn khóa học) - Dùng Combobox
tk.Label(root, text="Select course", bg="grey", font=font_label).place(x=80, y=370)
combo_course = ttk.Combobox(root, values=["Python", "Java", "C++", "Web"], width=27, font=font_entry)
combo_course.set("Select course") # Dòng chữ hiển thị ban đầu
combo_course.place(x=240, y=370)

# --- CÁC NÚT BẤM (BUTTONS) ---

# Nút Submit (Gọi hàm submit_form khi bấm)
btn_submit = tk.Button(root, text="Submit", bg="green", fg="white", font=("Arial", 12, "bold"), width=12,
                       command=submit_form)
btn_submit.place(x=120, y=450)

# Nút Cancel (Gọi hàm clear_form khi bấm)
btn_cancel = tk.Button(root, text="Cancel", bg="darkred", fg="white", font=("Arial", 12, "bold"), width=12,
                       command=clear_form)
btn_cancel.place(x=300, y=450)

# Chạy cửa sổ
root.mainloop()





































'''
ws = Tk()
ws.title('Registration Form')
ws.geometry('500x600')
ws.config(bg="grey")

f = ('Times', 12, 'bold')
var = StringVar()
var.set('male')

countries = []
variable = StringVar()
world = open("countries.txt", "r")
for country in world:
    country = country.strip('\n')
    countries.append(country)
    
right_frame = Frame(
    ws, bd=2, bg="grey",
    relief=SOLID, padx=10, pady=10
)

Label(
    right_frame, text="Họ tên:", bg="#CCCCCC", font=f
).grid(row=0,column=0, sticky=W, pady=10)   
Label(
    right_frame, text="Email:", bg="#CCCCCC", font=f
).grid(row=1,column=0, sticky=W, pady=10)
Label(
    right_frame, text="Ngày sinh:", bg="#CCCCCC", font=f
).grid(row=2,column=0, sticky=W, pady=10)
Label(
    right_frame, text="Chọn Quốc gia:", bg="#CCCCCC", font=f
).grid(row=3,column=0, sticky=W, pady=10)

gender_frame = Label(
    right_frame, bg="#CCCCCC", padx=10,pady=10,
)

txtName = Entry(right_frame,font=f)
txtEmail = Entry(right_frame,font=f)
dob = Entry(right_frame,font=f)
male_rb = Radiobutton(
    gender_frame, text='Nam', bg="#CCCCCC",
    variable=var,value='male', font=('Times',10),
)
female_rb = Radiobutton(
    gender_frame, text='Nữ', bg="#CCCCCC",
    variable=var,value='female', font=('Times',10),
)
other_rb = Radiobutton(
    gender_frame, text='Khác', bg="#CCCCCC",
    variable=var,value='other', font=('Times',10),
)
registercontries = OptionMenu(
    right_frame , variable, *countries
)
registercontries.config(font=('Times', 12), width=15)

def validateform():
    if txtName.get() == "":
        messagebox.showinfo("Lỗi", "Vui lòng nhập họ tên")
        txtName.focus_set()
        return
    if txtEmail.get() == "":
        messagebox.showinfo("Lỗi", "Vui lòng nhập email")
        txtEmail.focus_set()
        return
    if var.get() == "":
        messagebox.showinfo("Lỗi", "Vui lòng chọn giới tính")
        return  
    if variable.get() == "":
        messagebox.showinfo("Lỗi", "Vui lòng chọn quốc gia")
        return

registerButton = Button(
    right_frame, width=15, text="Đăng ký",
    font=f, relief=SOLID, cursor='hand2' ,command=validateform
)
txtName.grid(row=0,column=1, pady=10, padx=20)
txtEmail.grid(row=1,column=1, pady=10, padx=20)
dob.grid(row=2,column=1, pady=10, padx=20)
registercontries.grid(row=3,column=1, pady=10, padx=20)
registerButton.grid(row=5,column=1, pady=10, padx=20)
right_frame.pack()
gender_frame.grid(row=4,column=1, pady=10, padx=20)
male_rb.pack(expand=True,side=LEFT)
female_rb.pack(expand=True,side=LEFT)
other_rb.pack(expand=True,side=LEFT)

ws.mainloop()
'''



























'''
def validate_form():
    """
    Hàm kiểm tra dữ liệu đầu vào.
    Yêu cầu tất cả các trường không được để trống.
    """
    name = entry_name.get()
    email = entry_email.get()
    dob = entry_dob.get()
    gender = var_gender.get()
    contact = entry_contact.get()
    course = combo_course.get()

    # Kiểm tra xem có trường nào bị bỏ trống không
    if not name or not email or not dob or not contact or not course:
        messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ tất cả các thông tin!")
        return

    # Kiểm tra riêng trường Gender (Radio button)
    if gender == 0: # 0 là giá trị mặc định khi chưa chọn
        messagebox.showerror("Lỗi", "Vui lòng chọn Giới tính!")
        return

    # Nếu tất cả hợp lệ
    messagebox.showinfo("Thành công", f"Đăng ký thành công khóa học: {course}\nXin chào {name}!")

def clear_form():
    """Hàm xóa sạch dữ liệu trên form (Nút Cancel)"""
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_contact.delete(0, tk.END)
    combo_course.set('Select course')
    var_gender.set(0)

# --- Cấu hình cửa sổ chính ---
root = tk.Tk()
root.title("Registration Form")
root.geometry("500x600")
root.configure(bg="grey") # Màu nền xám như trong ảnh

# --- Tiêu đề (Header) ---
lbl_title = tk.Label(root, text="Course Registration form", 
                     bg="blue", fg="white", 
                     font=("Times New Roman", 20, "bold"),
                     width=30) # Độ rộng để tạo dải màu xanh
lbl_title.place(x=25, y=40)

# --- Các trường nhập liệu (Labels & Entries) ---
label_font = ("Times New Roman", 12, "bold")
bg_color = "grey"

# 1. Full Name
tk.Label(root, text="Full Name", bg=bg_color, font=label_font).place(x=80, y=120)
entry_name = tk.Entry(root, width=30, font=("Arial", 10))
entry_name.place(x=240, y=120)

# 2. Email
tk.Label(root, text="Email", bg=bg_color, font=label_font).place(x=80, y=170)
entry_email = tk.Entry(root, width=30, font=("Arial", 10))
entry_email.place(x=240, y=170)

# 3. DOB (Date of Birth)
tk.Label(root, text="DOB", bg=bg_color, font=label_font).place(x=80, y=220)
entry_dob = tk.Entry(root, width=30, font=("Arial", 10))
entry_dob.insert(0, "05/06/2020") # Giá trị mẫu như trong ảnh
entry_dob.place(x=240, y=220)

# 4. Gender
tk.Label(root, text="Gender", bg=bg_color, font=label_font).place(x=80, y=270)
var_gender = tk.IntVar() # Biến lưu giá trị radio button
r1 = tk.Radiobutton(root, text="Male", variable=var_gender, value=1, bg=bg_color, font=("Arial", 10, "bold"))
r1.place(x=240, y=270)
r2 = tk.Radiobutton(root, text="Female", variable=var_gender, value=2, bg=bg_color, font=("Arial", 10, "bold"))
r2.place(x=320, y=270)

# 5. Contact no.
tk.Label(root, text="Contact no.", bg=bg_color, font=label_font).place(x=80, y=320)
entry_contact = tk.Entry(root, width=30, font=("Arial", 10))
entry_contact.place(x=240, y=320)

# 6. Select course
tk.Label(root, text="Select course", bg=bg_color, font=label_font).place(x=80, y=370)
course_options = ["Python", "Java", "C++", "Web Development", "Data Science"]
combo_course = ttk.Combobox(root, values=course_options, width=27, font=("Arial", 10))
combo_course.set("Select course")
combo_course.place(x=240, y=370)

# --- Các nút chức năng (Buttons) ---
# Nút Submit (Màu xanh lá)
btn_submit = tk.Button(root, text="Submit", bg="green", fg="white", 
                       font=("Arial", 12, "bold"), width=12,
                       command=validate_form)
btn_submit.place(x=120, y=450)

# Nút Cancel (Màu đỏ)
btn_cancel = tk.Button(root, text="Cancel", bg="darkred", fg="white", 
                       font=("Arial", 12, "bold"), width=12,
                       command=clear_form)
btn_cancel.place(x=300, y=450)

# Chạy vòng lặp chính
root.mainloop()
'''
































'''
# ==========================================
# 1. MODEL: Xử lý logic và dữ liệu
# ==========================================
class RegistrationModel:
    def validate(self, data):
        # Kiểm tra các trường rỗng
        required_fields = ['name', 'email', 'dob', 'contact', 'course']
        for field in required_fields:
            if not data[field]:
                return False, "Vui lòng điền đầy đủ tất cả các thông tin!"

        # Kiểm tra giới tính (0 là chưa chọn)
        if data['gender'] == 0:
            return False, "Vui lòng chọn Giới tính!"

        # Nếu tất cả hợp lệ
        return True, f"Đăng ký thành công khóa học: {data['course']}\nXin chào {data['name']}!"

# ==========================================
# 2. VIEW: Xử lý giao diện hiển thị
# ==========================================
class RegistrationView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registration Form")
        self.geometry("500x600")
        self.configure(bg="grey")
        
        self._setup_ui()
    
    def _setup_ui(self):
        """Khởi tạo các widget giao diện"""
        label_font = ("Times New Roman", 12, "bold")
        bg_color = "grey"

        # Header
        lbl_title = tk.Label(self, text="Course Registration form", 
                             bg="blue", fg="white", 
                             font=("Times New Roman", 20, "bold"), width=30)
        lbl_title.place(x=25, y=40)

        # 1. Full Name
        tk.Label(self, text="Full Name", bg=bg_color, font=label_font).place(x=80, y=120)
        self.entry_name = tk.Entry(self, width=30, font=("Arial", 10))
        self.entry_name.place(x=240, y=120)

        # 2. Email
        tk.Label(self, text="Email", bg=bg_color, font=label_font).place(x=80, y=170)
        self.entry_email = tk.Entry(self, width=30, font=("Arial", 10))
        self.entry_email.place(x=240, y=170)

        # 3. DOB
        tk.Label(self, text="DOB", bg=bg_color, font=label_font).place(x=80, y=220)
        self.entry_dob = tk.Entry(self, width=30, font=("Arial", 10))
        self.entry_dob.insert(0, "05/06/2020")
        self.entry_dob.place(x=240, y=220)

        # 4. Gender
        tk.Label(self, text="Gender", bg=bg_color, font=label_font).place(x=80, y=270)
        self.var_gender = tk.IntVar()
        tk.Radiobutton(self, text="Male", variable=self.var_gender, value=1, 
                       bg=bg_color, font=("Arial", 10, "bold")).place(x=240, y=270)
        tk.Radiobutton(self, text="Female", variable=self.var_gender, value=2, 
                       bg=bg_color, font=("Arial", 10, "bold")).place(x=320, y=270)

        # 5. Contact
        tk.Label(self, text="Contact no.", bg=bg_color, font=label_font).place(x=80, y=320)
        self.entry_contact = tk.Entry(self, width=30, font=("Arial", 10))
        self.entry_contact.place(x=240, y=320)

        # 6. Course
        tk.Label(self, text="Select course", bg=bg_color, font=label_font).place(x=80, y=370)
        self.combo_course = ttk.Combobox(self, values=["Python", "Java", "C++", "Web"], 
                                         width=27, font=("Arial", 10))
        self.combo_course.set("Select course")
        self.combo_course.place(x=240, y=370)

        # Buttons (Chưa gán lệnh command ở đây, Controller sẽ gán sau)
        self.btn_submit = tk.Button(self, text="Submit", bg="green", fg="white", 
                                    font=("Arial", 12, "bold"), width=12)
        self.btn_submit.place(x=120, y=450)

        self.btn_cancel = tk.Button(self, text="Cancel", bg="darkred", fg="white", 
                                    font=("Arial", 12, "bold"), width=12)
        self.btn_cancel.place(x=300, y=450)

    def get_form_data(self):
        """Lấy dữ liệu từ giao diện để gửi cho Controller"""
        return {
            "name": self.entry_name.get(),
            "email": self.entry_email.get(),
            "dob": self.entry_dob.get(),
            "gender": self.var_gender.get(),
            "contact": self.entry_contact.get(),
            "course": self.combo_course.get()
        }

    def clear_form(self):
        """Xóa trắng giao diện"""
        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_dob.delete(0, tk.END)
        self.entry_contact.delete(0, tk.END)
        self.combo_course.set('Select course')
        self.var_gender.set(0)

    def show_message(self, title, message, is_error=False):
        """Hiển thị popup thông báo"""
        if is_error:
            messagebox.showerror(title, message)
        else:
            messagebox.showinfo(title, message)

# ==========================================
# 3. CONTROLLER: Điều phối hoạt động
# ==========================================
class RegistrationController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Gắn sự kiện (Event Binding)
        # Controller bảo View: "Khi nút Submit được bấm, hãy gọi hàm submit_handler của tôi"
        self.view.btn_submit.config(command=self.submit_handler)
        self.view.btn_cancel.config(command=self.cancel_handler)

    def submit_handler(self):
        # 1. Lấy dữ liệu từ View
        data = self.view.get_form_data()
        
        # 2. Gửi dữ liệu sang Model để kiểm tra
        is_valid, message = self.model.validate(data)

        # 3. Dựa vào kết quả Model trả về, bảo View hiển thị thông báo tương ứng
        if is_valid:
            self.view.show_message("Thành công", message, is_error=False)
        else:
            self.view.show_message("Lỗi", message, is_error=True)

    def cancel_handler(self):
        # Gọi hàm xóa form của View
        self.view.clear_form()

# ==========================================
# MAIN APP
# ==========================================
if __name__ == "__main__":
    # Khởi tạo các thành phần
    model = RegistrationModel()
    view = RegistrationView()
    
    # Controller kết nối Model và View
    controller = RegistrationController(model, view)

    # Chạy vòng lặp chính
    view.mainloop()
'''












































'''
from tkinter import *

root = Tk()
root.title("Form dang ky")
root.geometry('350x300')

lblName = Label(root, text="Ho va ten:").place(x=40,y=60)
lblAge = Label(root, text="Tuoi:").place(x=40,y=100)
lblAddress = Label(root, text="Dia chi:").place(x=40,y=140)

txtName = Entry(root, width=30).place(x=110,y=60)
txtAge = Entry(root, width=30).place(x=110,y=100)
txtAddress = Entry(root, width=30).place(x=110, y=140)

btnRegister = Button(root, text="Dang Ky", command= root.destroy).place(x =70, y=180)

root.mainloop()
'''