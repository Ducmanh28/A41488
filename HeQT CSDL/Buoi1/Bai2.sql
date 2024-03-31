use master
go

create database QUANLY
go

use QUANLY
go
------------------------------------------------------------------------------------------
-- Tạo các bảng

CREATE TABLE NHAN_VIEN (
    MaNV INT PRIMARY KEY,
    Ho NVARCHAR(50),
    Ten NVARCHAR(50),
    NgaySinh DATE,
    NgayLamViec DATE,
    DiaChi NVARCHAR(100),
    LuongCoBan DECIMAL(18, 2),
    PhuCap DECIMAL(18, 2)
);

CREATE TABLE KHACH_HANG (
    MaKH INT PRIMARY KEY,
    TenCongTy NVARCHAR(100),
    TenGiaoDich NVARCHAR(100),
    DiaChi NVARCHAR(100),
    Email NVARCHAR(100),
    DienThoai NVARCHAR(20),
    Fax NVARCHAR(20)
);

CREATE TABLE NHA_CUNG_CAP (
    MaCT INT PRIMARY KEY,
    TenCongTy NVARCHAR(100),
    TenGiaoDich NVARCHAR(100),
    DiaChi NVARCHAR(100),
    DienThoai NVARCHAR(20),
    Fax NVARCHAR(20),
    Email NVARCHAR(100)
);

CREATE TABLE LOAI_HANG (
    MaLoaiHang INT PRIMARY KEY,
    TenLoaiHang NVARCHAR(100)
);

CREATE TABLE MAT_HANG (
    MaHang INT PRIMARY KEY,
    TenHang NVARCHAR(100),
    MaCT INT,
    MaLoaiHang INT,
    SoLuong INT,
    DonViTinh NVARCHAR(50),
    GiaHang DECIMAL(18, 2),
    FOREIGN KEY (MaCT) REFERENCES NHA_CUNG_CAP(MaCT),
    FOREIGN KEY (MaLoaiHang) REFERENCES LOAI_HANG(MaLoaiHang)
);

CREATE TABLE DON_DAT_HANG (
    SoHoaDon INT PRIMARY KEY,
    MaKH INT,
    MaNV INT,
    NgayDatHang DATE,
    NgayGiaoHang DATE,
    NgayChuyenHang DATE,
    NoiGiaoHang NVARCHAR(100),
    FOREIGN KEY (MaKH) REFERENCES KHACH_HANG(MaKH),
    FOREIGN KEY (MaNV) REFERENCES NHAN_VIEN(MaNV)
);

CREATE TABLE CHI_TIET_DAT_HANG (
    SoHoaDon INT,
    MaHang INT,
    GiaBan DECIMAL(18, 2),
    SoLuong INT,
    MucGiamGia DECIMAL(18, 2),
    PRIMARY KEY (SoHoaDon, MaHang),
    FOREIGN KEY (SoHoaDon) REFERENCES DON_DAT_HANG(SoHoaDon),
    FOREIGN KEY (MaHang) REFERENCES MAT_HANG(MaHang)
);
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- Bắt đầu chèn dữ liệu vào các bảng

Insert into KHACH_HANG(MaKH, TenCongTy, TenGiaoDich, DiaChi, Email, DienThoai, Fax) values (1,'A','A','12 Nguyễn Sinh Cung','a@yahoo.com','054.523456','054.523457')
Insert into KHACH_HANG(MaKH, TenCongTy, TenGiaoDich, DiaChi, Email, DienThoai, Fax) values (2,'B','B','34 Nguyễn Thiện Thuật','b@yahoo.com','060.123456','060.123457')
Insert into KHACH_HANG(MaKH, TenCongTy, TenGiaoDich, DiaChi, Email, DienThoai, Fax) values (3,'C','C','67/3 Lê Hữu Trác','c@yahoo.com','0511.876564','0511.876566')
Insert into KHACH_HANG(MaKH, TenCongTy, TenGiaoDich, DiaChi, Email, DienThoai, Fax) values (4,'D','D','234/23 Lê Văn Hưu','d@yahoo.com','061.567894','061.567898')
Insert into KHACH_HANG(MaKH, TenCongTy, TenGiaoDich, DiaChi, Email, DienThoai, Fax) values (5,'E','E','12 Nguyễn Văn Linh','e@yahoo.com','054.826456','054.826456')
Insert into KHACH_HANG(MaKH, TenCongTy, TenGiaoDich, DiaChi, Email, DienThoai, Fax) values (6,'F','F','123 Lê Quý Đôn','f@yahoo.com','054.826456','054.826456')

Insert into NHAN_VIEN(MaNV, Ho, Ten, NgaySinh, NgayLamViec, DiaChi, LuongCoBan, PhuCap) values (1,'Nguyễn Văn','Phú','1958-12-12','1978-11-01','245 Lê Văn Hưu',1456789,456589)
Insert into NHAN_VIEN(MaNV, Ho, Ten, NgaySinh, NgayLamViec, DiaChi, LuongCoBan, PhuCap) values (2,'Lê Đại','Dương','1934-01-01','1960-01-23','123 Lê Văn Hưu',24564564,787788)
Insert into NHAN_VIEN(MaNV, Ho, Ten, NgaySinh, NgayLamViec, DiaChi, LuongCoBan, PhuCap) values (3,'Phan Văn','Hùng','1968-11-23','1980-10-01','12/4 Lê Văn Hưu',12312341,686668)
Insert into NHAN_VIEN(MaNV, Ho, Ten, NgaySinh, NgayLamViec, DiaChi, LuongCoBan, PhuCap) values (4,'Nguyễn Văn','Thành','1965-12-12','1985-10-01','1234 Lê Duẩn',35454545,454454)
Insert into NHAN_VIEN(MaNV, Ho, Ten, NgaySinh, NgayLamViec, DiaChi, LuongCoBan, PhuCap) values (5,'Lê Khánh','Đạt','1948-07-31','1965-10-01','12 ABC',44353555,445444)
Insert into NHAN_VIEN(MaNV, Ho, Ten, NgaySinh, NgayLamViec, DiaChi, LuongCoBan, PhuCap) values (6,'Nguyễn Thị','Huyền','1960-12-23','1980-01-01','23 BC',23242342,454544)

Insert into DON_DAT_HANG(SoHoaDon, MaKH,MaNV, NgayDatHang, NgayGiaoHang, NgayChuyenHang, NoiGiaoHang) values (1,1,1,'2005-05-12','2005-05-18','2005-05-18','Nguyễn Sinh Cung')
Insert into DON_DAT_HANG(SoHoaDon, MaKH,MaNV, NgayDatHang, NgayGiaoHang, NgayChuyenHang, NoiGiaoHang) values (2,2,4,'2005-12-13','2006-01-17',' ','Nguyễn Thiện Thuật')
Insert into DON_DAT_HANG(SoHoaDon, MaKH,MaNV, NgayDatHang, NgayGiaoHang, NgayChuyenHang, NoiGiaoHang) values (3,4,1,'2005-10-01','2005-10-02',' ','Huế')
Insert into DON_DAT_HANG(SoHoaDon, MaKH,MaNV, NgayDatHang, NgayGiaoHang, NgayChuyenHang, NoiGiaoHang) values (4,5,2,'2005-10-23','2005-11-01',' ','Đà Nẵng')
Insert into DON_DAT_HANG(SoHoaDon, MaKH,MaNV, NgayDatHang, NgayGiaoHang, NgayChuyenHang, NoiGiaoHang) values (5,1,1,'1998-07-28','1998-07-29','1998-07-29','Sài Gòn')
Insert into DON_DAT_HANG(SoHoaDon, MaKH,MaNV, NgayDatHang, NgayGiaoHang, NgayChuyenHang, NoiGiaoHang) values (6,2,2,'2000-01-01','2000-01-02',' ','Nha Trang')

Insert into LOAI_HANG(MaLoaiHang,TenLoaiHang) values (1,'A')
Insert into LOAI_HANG(MaLoaiHang,TenLoaiHang) values (2,'B')
Insert into LOAI_HANG(MaLoaiHang,TenLoaiHang) values (3,'C')
Insert into LOAI_HANG(MaLoaiHang,TenLoaiHang) values (4,'D')
Insert into LOAI_HANG(MaLoaiHang,TenLoaiHang) values (5,'E')
Insert into LOAI_HANG(MaLoaiHang,TenLoaiHang) values (6,'F')

Insert into NHA_CUNG_CAP(MaCT, TenCongTy, TenGiaoDich, DiaChi, DienThoai, Fax, Email) values (1,'AB','AB','12 Trần Hưng Đạo','0511.1234567','0511.1234568','ab@yahoo.com')
Insert into NHA_CUNG_CAP(MaCT, TenCongTy, TenGiaoDich, DiaChi, DienThoai, Fax, Email) values (2,'AC','AC','123/5 Lê Văn Hưu','0510.1344567','0510.1344568','ac@yahoo.com')
Insert into NHA_CUNG_CAP(MaCT, TenCongTy, TenGiaoDich, DiaChi, DienThoai, Fax, Email) values (3,'AD','AD','12 Lê Duẩn','054.541239','054.541239','ad@yahoo.com')
Insert into NHA_CUNG_CAP(MaCT, TenCongTy, TenGiaoDich, DiaChi, DienThoai, Fax, Email) values (4,'A','A','2/1 Trần Hưng Đạo','054.528678','054.528678','a@yahoo.com')
Insert into NHA_CUNG_CAP(MaCT, TenCongTy, TenGiaoDich, DiaChi, DienThoai, Fax, Email) values (5,'B','B','30 Trần Hưng Đạo','0511.8234567','0511.8234567','b@yahoo.com')
Insert into NHA_CUNG_CAP(MaCT, TenCongTy, TenGiaoDich, DiaChi, DienThoai, Fax, Email) values (6,'H','H','5 Lê Thánh Tôn','0510.8734567','0510.8734567','h@yahoo.com')

Insert into MAT_HANG(MaHang, TenHang, MaCT, MaLoaiHang, SoLuong, DonViTinh, GiaHang) values (1,'Đĩa cứng',1,1,28,'cái',4000000)
Insert into MAT_HANG(MaHang, TenHang, MaCT, MaLoaiHang, SoLuong, DonViTinh, GiaHang) values (2,'Đĩa mềm',2,2,245,'cái',5000)
Insert into MAT_HANG(MaHang, TenHang, MaCT, MaLoaiHang, SoLuong, DonViTinh, GiaHang) values (3,'Cổng USB',1,3,21,'cái',250000)
Insert into MAT_HANG(MaHang, TenHang, MaCT, MaLoaiHang, SoLuong, DonViTinh, GiaHang) values (4,'Màn hình',3,4,5,'cái',2000000)
Insert into MAT_HANG(MaHang, TenHang, MaCT, MaLoaiHang, SoLuong, DonViTinh, GiaHang) values (5,'Bàn phím',4,5,45,'cái',100000)
Insert into MAT_HANG(MaHang, TenHang, MaCT, MaLoaiHang, SoLuong, DonViTinh, GiaHang) values (6,'Đĩa CD',5,6,58,'cái',3000)

Insert into CHI_TIET_DAT_HANG(SoHoaDon, MaHang, GiaBan, SoLuong, MucGiamGia) values (1,1,4200000,2,10)
Insert into CHI_TIET_DAT_HANG(SoHoaDon, MaHang, GiaBan, SoLuong, MucGiamGia) values (1,2,8000,12,5)
Insert into CHI_TIET_DAT_HANG(SoHoaDon, MaHang, GiaBan, SoLuong, MucGiamGia) values (2,2,8000,2,5)
Insert into CHI_TIET_DAT_HANG(SoHoaDon, MaHang, GiaBan, SoLuong, MucGiamGia) values (3,3,300000,5,0)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- Bắt đầu truy vấn
----------------------------------------
-- Tìm tất cả khách hàng có mã từ 2-4
-- Cách AND:
Select * from KHACH_HANG 
where MaKH>=2 and MaKH <= 4;
-- Cách BETWEEN
Select * from KHACH_HANG
where MaKH BETWEEN 2 and 4;
---------------------------------------
-- Tìm những mặt hàng có giá < 150000
Select * from MAT_HANG
where GiaHang < 150000
---------------------------------------
-- Tìm ra những mặt hàng có đơn vị tính >= 20
Select * from MAT_HANG where SoLuong >= 20
-----------------------------------------
--Tìm ra những nhân viên có họ Nguyễn 
Select * from NHAN_VIEN 
where Ho like 'Nguyễn%';
---------------------------------------------
-- Tìm giá nhỏ nhất và giá lớn nhất của Mặt hàng
Select MIN(GiaHang) as GiaNhoNhat,MAX(GiaHang) as GiaLonNhat from MAT_HANG;