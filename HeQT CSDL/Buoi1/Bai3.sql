use master
go
-- Tạo Database
create database QUANLYBANPHIM;
use QUANLYBANPHIM;
go
------------------------------------------------------------------------
-- Bắt đầu tạo các bảng
CREATE TABLE THE_LOAI (
    MTL INT IDENTITY(1,1) PRIMARY KEY,
    Ten_the_loai NVARCHAR(50)
);

CREATE TABLE KHACH_HANG (
    MKH INT IDENTITY(1,1) PRIMARY KEY,
    Ho_khach_hang NVARCHAR(50),
    Ten_khach_hang NVARCHAR(20),
    Ten_dang_nhap VARCHAR(20),
    Mat_khau VARCHAR(20),
    Gioi_tinh BIT,
    Dia_chi NVARCHAR(100),
    Email VARCHAR(20),
    Quan_tri BIT
);

CREATE TABLE PHIM (
    MP INT IDENTITY(1,1) PRIMARY KEY,
    Ten_phim NVARCHAR(100),
    Ten_tieng_ANH VARCHAR(100),
    Noi_dung NTEXT,
    Dien_vien NVARCHAR(100),
    Hinh_minh_hoa VARCHAR(50),
    Hang_san_xuat NVARCHAR(100),
    Ngay_cap_nhat DATETIME,
    Don_gia INT,
    So_luong INT
);

CREATE TABLE PHIM_THE_LOAI (
    MP INT,
    MTL INT,
    PRIMARY KEY (MP, MTL),
    CONSTRAINT KEY_1 FOREIGN KEY (MP) REFERENCES PHIM(MP),
    CONSTRAINT KEY_2 FOREIGN KEY (MTL) REFERENCES THE_LOAI(MTL)
);

CREATE TABLE DAT_HANG (
    MDH INT IDENTITY(1,1) PRIMARY KEY,
    MKH INT,
    Ngay_dat DATETIME,
    Ngay_giao DATETIME,
    Ghi_chu NVARCHAR(100),
    CONSTRAINT KEY_3 FOREIGN KEY (MKH) REFERENCES KHACH_HANG(MKH)
);

CREATE TABLE CT_DAT_HANG (
    MCT INT IDENTITY(1,1) PRIMARY KEY,
    MDH INT,
    MP INT,
    So_luong INT,
    CONSTRAINT KEY_4 FOREIGN KEY (MDH) REFERENCES DAT_HANG(MDH),
    CONSTRAINT KEY_5 FOREIGN KEY (MP) REFERENCES PHIM(MP)
);

CREATE TABLE GOP_Y (
    MGY INT IDENTITY(1,1) PRIMARY KEY,
    Ho_ten NVARCHAR(100),
    MKH INT,
    Noi_dung NTEXT,
    Dien_thoai VARCHAR(20),
    Email VARCHAR(20),
    CONSTRAINT KEY_6 FOREIGN KEY (MKH) REFERENCES KHACH_HANG(MKH)
);

CREATE TABLE QUANG_CAO (
    MQC INT IDENTITY(1,1) PRIMARY KEY,
    Ngay_bat_dau DATETIME,
    Ngay_ket_thuc DATETIME,
    Hinh_minh_hoa VARCHAR(100),
    Duong_dan VARCHAR(100)
);
--------------------------------------------------------------------------------------
-- Bắt đầu chèn thông tin vào các bảng

INSERT INTO DAT_HANG (MKH, Ngay_dat, Ngay_giao, Ghi_chu) VALUES 
(1, '2023-03-08', '2023-03-08', 'Giao nhanh'),
(2, '2023-01-02', '2023-01-05', 'Không cần gói quà'),
(3, '2023-02-04', '2023-02-07', 'Giao trong ngày'),
(4, '2023-11-04', '2023-11-08', 'Giao trước 9h sáng'),
(5, '2024-01-05', '2024-01-09', 'Liên hệ trước khi giao');

INSERT INTO CT_DAT_HANG (MDH, MP, So_luong) VALUES 
(1, 1, 2),
(2, 2, 1),
(3, 3, 3),
(4, 4, 1),
(5, 5, 2);

INSERT INTO GOP_Y (Ho_ten, MKH, Noi_dung, Dien_thoai, Email) VALUES 
('Nguyen Van A', 1, 'Hài lòng với sản phẩm', '0123456789', 'a@example.com'),
('Le Thi B', 2, 'Giao hàng chậm', '0123456790', 'b@example.com'),
('Dinh Van C', 3, 'Phim hay', '0123456781', 'c@example.com'),
('Nguyen Thi D', 4, 'Đóng gói cẩn thận', '0123456782', 'd@example.com'),
('Kem Van E', 5, 'Cần nhiều phim mới', '0123456783', 'e@example.com');

INSERT INTO QUANG_CAO (Ngay_bat_dau, Ngay_ket_thuc, Hinh_minh_hoa, Duong_dan) VALUES 
('2022-01-28', '2023-03-01', 'hinhanh1.jpg', 'http://vidu.com/hinh1'),
('2023-02-20', '2023-04-01', 'hinhanh2.jpg', 'http://vidu.com/hinh2'),
('2022-03-03', '2023-05-01', 'hinhanh3.jpg', 'http://vidu.com/hinh3'),
('2023-04-05', '2023-06-01', 'hinhanh4.jpg', 'http://vidu.com/hinh4'),
('2021-07-08', '2023-07-01', 'hinhanh5.jpg', 'http://vidu.com/hinh5');

INSERT INTO THE_LOAI (Ten_the_loai) VALUES 
('Hành Động'), 
('Hài'), 
('Kinh Dị'), 
('Tình Cảm'), 
('Phiêu Lưu');

INSERT INTO KHACH_HANG (Ho_khach_hang, Ten_khach_hang, Ten_dang_nhap, Mat_khau, Gioi_tinh, Dia_chi, Email, Quan_tri) VALUES 
('Nguyen', 'Van A', 'abc', 'pass1', 1, 'Thanh Hoa', 'abc@example.com', 0),
('Le', 'Thi B', 'bcd', 'pass2', 0, 'Ha Noi', 'bcd@example.com', 0),
('Dinh', 'Van C', 'cde', 'pass3', 1, 'Da Nang', 'cde@example.com', 0),
('Nguyen', 'Thi D', 'def', 'pass4', 0, 'Can Tho', 'def@example.com', 0),
('Kem', 'Van E', 'efg', 'pass5', 1, 'Hai Phong', 'efg@example.com', 0);

INSERT INTO PHIM (Ten_phim, Ten_tieng_ANH, Noi_dung, Dien_vien, Hinh_minh_hoa, Hang_san_xuat, Ngay_cap_nhat, Don_gia, So_luong) VALUES 
('Phim Hành Động A', 'Action Movie', 'Nội dung hành động', 'DV_1', 'hinhanh1.jpg', 'Hãng sản xuất A', '2023-01-09', 135000, 36),
('Phim Hài B', 'Comedy Movie', 'Nội dung hài', 'DV_2', 'hinhanh2.jpg', 'Hãng sản xuất B', '2023-03-21', 89000, 46),
('Phim Kinh Dị C', 'Horror Movie', 'Nội dung kinh dị', 'DV_3', 'hinhanh3.jpg', 'Hãng sản xuất C', '2023-11-20', 226000, 29),
('Phim Tình Cảm D', 'Romantic Movie', 'Nội dung tình cảm', 'DV_4', 'hinhanh4.jpg', 'Hãng sản xuất D', '2023-07-21', 75000, 63),
('Phim Phiêu Lưu E', 'Adventure Movie', 'Nội dung phiêu lưu', 'DV_5', 'hinhanh5.jpg', 'Hãng sản xuất E', '2023-12-31', 115000, 21);

INSERT INTO PHIM_THE_LOAI (MP, MTL) VALUES 
(1, 1), 
(2, 2), 
(3, 3), 
(4, 4), 
(5, 5);
------------------------------------------------------------------------------------------------------------------------------------------
-- Bắt đầu thực hiện truy vấn
---------------------------------------------------------
-- Tìm tất cả các phim có số lượng từ 20 đến 50
SELECT * FROM PHIM WHERE So_luong BETWEEN 20 AND 50;
---------------------------------------------------------
-- Tìm tất cả các phim có tên bắt đầu bằng chữ "Kiếm"
SELECT * FROM PHIM WHERE Ten_phim LIKE 'Kiếm%';
--------------------------------------------------------
-- Tìm 2 khách hàng đầu tiên trong bảng KHACH_HANG
SELECT TOP 2 * FROM KHACH_HANG ORDER BY MKH;
--------------------------------------------------------
-- Tìm thông tin của các khách hàng có giới tính là nam và đếm tổng số khách hàng này
SELECT *, (SELECT COUNT(*) FROM KHACH_HANG WHERE Gioi_tinh = 1) AS Tong_So_Nam FROM KHACH_HANG WHERE Gioi_tinh = 1;
--------------------------------------------------------
-- Tìm chi tiết về phim có mức giá lớn nhất và nhỏ nhất
SELECT * FROM PHIM WHERE Don_gia = (SELECT MAX(Don_gia) FROM PHIM)
UNION
SELECT * FROM PHIM WHERE Don_gia = (SELECT MIN(Don_gia) FROM PHIM);
---------------------------------------------------------
-- Tính tổng giá và giá trung bình của các phim
SELECT SUM(Don_gia) AS Tong_Gia, AVG(Don_gia) AS Gia_Trung_Binh FROM PHIM;
---------------------------------------------------------
-- Tìm tất cả phim do diễn viên “Lâm Chí Linh” thủ vai
SELECT * FROM PHIM WHERE Dien_vien LIKE '%Lâm Chí Linh%';
---------------------------------------------------------
-- Xóa thông tin về những phim có giá <15.000 VND
DELETE FROM PHIM WHERE Don_gia < 15000;
---------------------------------------------------------
-- Sửa thông tin về những phim có giá =30.000 VND trở thành giá = 40.000
UPDATE PHIM SET Don_gia = 40000 WHERE Don_gia = 30000;