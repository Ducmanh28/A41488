import tkinter
from tkinter import messagebox

class A:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('500x500')
        
        self.frame1 = tkinter.Label(self.root,width=400,height=400,bg='#AAAAAA')
        self.frame1.pack()
        
# create menu
    def popup(self):
        self.popup_menu = tkinter.Menu(self.root, tearoff=0)

        self.popup_menu.add_command(label="Thêm mới", command=lambda: self.hey("Thêm mới"))
        self.popup_menu.add_command(label="Cập nhật", command=lambda: self.hey("Cập nhật"))
        self.popup_menu.add_command(label="Xóa", command=lambda: self.hey("Xóa"))
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label="Kết thúc", command=lambda: self.quit())

    # display menu on right click
    def do_popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.popup_menu.grab_release()

    def hey(self, s):
        self.frame1.configure(text=s)

    def quit(self):
        res = messagebox.askquestion('Xác nhận thoát !', 'Bạn có thực sự muốn thoát ?')
        if res == 'yes':
            self.root.destroy()
        else:
            return

    def run(self):
        self.popup()
        self.root.bind("<Button-3>", self.do_popup)
        tkinter.mainloop()

obj = A()
obj.run()