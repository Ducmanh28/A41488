import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

# Hàm lưu dữ liệu vào SQLite
def save_data():
    firstname = entry_firstname.get().strip()
    lastname = entry_lastname.get().strip()
    gender = gender_var.get()
    address = entry_address.get().strip()
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    # Kiểm tra dữ liệu nhập vào
    if not firstname or not lastname or not address or not username or not password:
        messagebox.showerror("Lỗi", "Tất cả các trường đều phải nhập!")
        return

    if not gender:
        messagebox.showerror("Lỗi", "Phải chọn giới tính!")
        return

    if not (6 <= len(password) <= 30 and re.search(r'\W', password)):
        messagebox.showerror("Lỗi", "Mật khẩu phải có từ 6-30 ký tự và chứa ít nhất một ký tự đặc biệt!")
        return

    # Lưu vào SQLite
    try:
        conn = sqlite3.connect("employeemanagement.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employee (firstname, lastname, gender, address, username, password) VALUES (?, ?, ?, ?, ?, ?)",
                       (firstname, lastname, gender, address, username, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Đăng ký thành công!")
        load_data()
    except sqlite3.IntegrityError:
        messagebox.showerror("Lỗi", "Username đã tồn tại!")

# Hàm tải dữ liệu lên Listbox
def load_data():
    listbox.delete(0, tk.END)
    conn = sqlite3.connect("employeemanagement.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, firstname, lastname, gender, address FROM employee")
    for row in cursor.fetchall():
        listbox.insert(tk.END, row)
    conn.close()

# Hàm xóa dữ liệu
def delete_data():
    try:
        selected = listbox.get(listbox.curselection())
        emp_id = selected[0]
        conn = sqlite3.connect("employeemanagement.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employee WHERE id=?", (emp_id,))
        conn.commit()
        conn.close()
        load_data()
        messagebox.showinfo("Thành công", "Xóa thành công!")
    except:
        messagebox.showerror("Lỗi", "Chọn một nhân viên để xóa!")

# Hàm đóng ứng dụng
def exit_app():
    if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn thoát?"):
        root.quit()

# Giao diện Tkinter
root = tk.Tk()
root.title("Python: Simple CRUD Application")

# Labels và Entry
tk.Label(root, text="Firstname:").grid(row=0, column=0)
entry_firstname = tk.Entry(root)
entry_firstname.grid(row=0, column=1)

tk.Label(root, text="Lastname:").grid(row=1, column=0)
entry_lastname = tk.Entry(root)
entry_lastname.grid(row=1, column=1)

tk.Label(root, text="Gender:").grid(row=2, column=0)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=2, sticky="w")

tk.Label(root, text="Address:").grid(row=3, column=0)
entry_address = tk.Entry(root)
entry_address.grid(row=3, column=1)

tk.Label(root, text="Username:").grid(row=4, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=4, column=1)

tk.Label(root, text="Password:").grid(row=5, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=5, column=1)

# Listbox hiển thị dữ liệu
listbox = tk.Listbox(root, width=50)
listbox.grid(row=0, column=3, rowspan=6)

# Buttons
tk.Button(root, text="Create", command=save_data).grid(row=6, column=0)
tk.Button(root, text="Read", command=load_data).grid(row=6, column=1)
tk.Button(root, text="Delete", command=delete_data).grid(row=6, column=2)
tk.Button(root, text="Exit", command=exit_app).grid(row=6, column=3)

# Load dữ liệu ban đầu
load_data()

root.mainloop()
