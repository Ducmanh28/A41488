import sqlite3

# Kết nối đến SQLite
conn = sqlite3.connect("quan_ly_sinh_vien.db")
cursor = conn.cursor()

# Tạo bảng KHOA
cursor.execute("""
CREATE TABLE IF NOT EXISTS KHOA (
    MaKH TEXT PRIMARY KEY,
    TenKH TEXT(50)
)
""")

# Tạo bảng MON
cursor.execute("""
CREATE TABLE IF NOT EXISTS MON (
    MaMH TEXT PRIMARY KEY,
    TenMH TEXT(25),
    SoTiet INTEGER
)
""")

# Tạo bảng SINHVIEN
cursor.execute("""
CREATE TABLE IF NOT EXISTS SINHVIEN (
    MaSV TEXT PRIMARY KEY,
    HoSV TEXT(15),
    TenSV TEXT(7),
    Phai TEXT CHECK(Phai IN ('Nam', 'Nữ')),
    NgaySinh TEXT,
    NoiSinh TEXT(15),
    MaKH TEXT,
    HocBong REAL,
    FOREIGN KEY (MaKH) REFERENCES KHOA(MaKH)
)
""")

# Tạo bảng KETQUA
cursor.execute("""
CREATE TABLE IF NOT EXISTS KETQUA (
    MaSV TEXT,
    MaMH TEXT,
    Diem REAL,
    PRIMARY KEY (MaSV, MaMH),
    FOREIGN KEY (MaSV) REFERENCES SINHVIEN(MaSV),
    FOREIGN KEY (MaMH) REFERENCES MON(MaMH)
)
""")
cursor.executemany("INSERT INTO KHOA (MaKH, TenKH) VALUES (?, ?)", [
    ('AV', 'Anh Văn'),
    ('TH', 'Tin Học'),
    ('TR', 'Triết')
])

# Chèn dữ liệu mẫu vào bảng MON
cursor.executemany("INSERT INTO MON (MaMH, TenMH, SoTiet) VALUES (?, ?, ?)", [
    ('01', 'Cơ sở dữ liệu', 45),
    ('02', 'Trí tuệ nhân tạo', 45),
    ('03', 'Truyền tin', 45),
    ('04', 'Đồ họa', 60),
    ('05', 'Văn phạm', 60)
])

# Chèn dữ liệu mẫu vào bảng SINHVIEN
cursor.executemany("INSERT INTO SINHVIEN (MaSV, HoSV, TenSV, Phai, NgaySinh, NoiSinh, MaKH, HocBong) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", [
    ('A01', 'Nguyễn thị', 'Hải', 'Nữ', '23/02/1977', 'Hà Nội', 'TH', 130000),
    ('A02', 'Trần văn', 'Chính', 'Nam', '24/12/1977', 'Bình Định', 'TH', 150000),
    ('A03', 'Lê thu bạch', 'Yến', 'Nữ', '21/02/1977', 'Tp HCM', 'TH', 170000),
    ('A04', 'Trần anh', 'Tuấn', 'Nam', '20/12/1977', 'Hà Nội', 'AV', 80000),
    ('B01', 'Trần thanh', 'Mai', 'Nữ', '12/08/1977', 'Hải Phòng', 'TR', 0),
    ('B02', 'Trần thị thu', 'Thủy', 'Nữ', '02/01/1977', 'Tp HCM', 'AV', 0)
])

# Chèn dữ liệu mẫu vào bảng KETQUA
cursor.executemany("INSERT INTO KETQUA (MaSV, MaMH, Diem) VALUES (?, ?, ?)", [
    ('A01', '01', 3), ('A01', '02', 6), ('A01', '03', 5), ('A01', '04', 4.5),
    ('A02', '03', 10), ('A02', '05', 9), ('A03', '01', 2), ('A03', '03', 2.5),
    ('A04', '05', 10), ('B01', '03', 2.5), ('B02', '02', 6), ('B02', '04', 10)
])

# In ra 3 sinh viên có học bổng cao nhất
cursor.execute("SELECT * FROM SINHVIEN ORDER BY HocBong DESC LIMIT 3")
print("3 Sinh vien co hoc bong cao nhat: ",cursor.fetchall())

# Tìm ra sinh viên có tên bắt đầu bằng chữ 'T'
cursor.execute("SELECT * FROM SINHVIEN WHERE TenSV LIKE 'T%'")
print("Sinh vien co ten bat dau bang T",cursor.fetchall())


# Cập nhật sinh viên có mã A05: Đổi tên thành 'Tony Nguyễn'
cursor.execute("UPDATE SINHVIEN SET HoSV = 'Tony', TenSV = 'Nguyễn' WHERE MaSV = 'A05'")
print("Cap nhat sinh vien thanh cong")

# Xóa sinh viên có học bổng = 0
cursor.execute("DELETE FROM SINHVIEN WHERE HocBong = 0")
print("Xoa sinh vien thanh cong!")

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()

