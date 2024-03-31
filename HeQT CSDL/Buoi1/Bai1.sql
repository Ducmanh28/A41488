-- TẠO DATABASE
create database QUANLYRAPPHIM

-- SỬ DỤNG DATABASE
use QUANLYRAPPHIM

-- TẠO BẢNG
create table tblRAP(
	MA_RAP char (2),
	TEN_RAP Nvarchar (60),
	DIA_CHI Nvarchar (100)
)

create table tblPHIM(
	MA_PHIM char (5),
	TEN_PHIM Nvarchar (100),
	MA_THE_LOAI int,
	NGAY_PHAT_HANH datetime,
	HANG_SAN_XUAT Nvarchar (100)
)

create table tblLC(
	MA_LICH int,
	MA_RAP Char (2),
	MA_PHIM char(5),
	THOI_GIAN datetime,
	SO_LUONG_VE smallint
)

-- Tạo dữ liệu cho bảng Rạp
insert into tblRAP (MA_RAP, TEN_RAP, DIA_CHI) values ('B1','BETA CINEMAX','THANH XUAN');
insert into tblRAP (MA_RAP, TEN_RAP, DIA_CHI) values ('B2','BETA CINEMAX','MY DINH');
insert into tblRAP (MA_RAP, TEN_RAP, DIA_CHI) values ('B3','BETA CINEMAX','GIAI PHONG');
insert into tblRAP (MA_RAP, TEN_RAP, DIA_CHI) values ('B4','BETA CINEMAX','TU LIEM');
insert into tblRAP (MA_RAP, TEN_RAP, DIA_CHI) values ('B5','BETA CINEMAX','CAU GIAY');
insert into tblRAP (MA_RAP, TEN_RAP, DIA_CHI) values ('C1','CGV','NGUYEN CHI THANH');
insert into tblRAP (MA_RAP, TEN_RAP, DIA_CHI) values ('C2','CGV','HO TUNG MAU');
insert into tblRAP (MA_RAP, TEN_RAP, DIA_CHI) values ('C3','CGV','DUONG CAU GIAY');
insert into tblRAP (MA_RAP, TEN_RAP, DIA_CHI) values ('C4','CGV','LE VAN LUONG');
insert into tblRAP (MA_RAP, TEN_RAP, DIA_CHI) values ('C5','CGV','TO HUU');
insert into tblRAP (MA_RAP, TEN_RAP, DIA_CHI) values ('MG','MegaStar','NGUYEN XIEN');

-- Tạo dữ liệu cho bảng PHIM
INSERT INTO tblPHIM (MA_PHIM, TEN_PHIM, MA_THE_LOAI, NGAY_PHAT_HANH, HANG_SAN_XUAT) VALUES ('PH1', 'MegaStar', 1, '2023-05-10', 'ABC Productions');
INSERT INTO tblPHIM (MA_PHIM, TEN_PHIM, MA_THE_LOAI, NGAY_PHAT_HANH, HANG_SAN_XUAT) VALUES ('PH2', 'Sex Is Zero', 2, '2002-12-12', 'XYZ Studios');
INSERT INTO tblPHIM (MA_PHIM, TEN_PHIM, MA_THE_LOAI, NGAY_PHAT_HANH, HANG_SAN_XUAT) VALUES ('PH3', 'Xác Ướp Ai Cập', 3, '1999-07-23', 'DEF Entertainment');
INSERT INTO tblPHIM (MA_PHIM, TEN_PHIM, MA_THE_LOAI, NGAY_PHAT_HANH, HANG_SAN_XUAT) VALUES ('PH4', 'Some Random Movie', 1, '2010-08-15', 'GHI Pictures');
INSERT INTO tblPHIM (MA_PHIM, TEN_PHIM, MA_THE_LOAI, NGAY_PHAT_HANH, HANG_SAN_XUAT) VALUES ('PH5', 'Another Film', 2, '2015-03-28', 'JKL Studios');
INSERT INTO tblPHIM (MA_PHIM, TEN_PHIM, MA_THE_LOAI, NGAY_PHAT_HANH, HANG_SAN_XUAT) VALUES ('PH6', 'Action Thriller', 3, '2018-11-07', 'MNO Productions');
INSERT INTO tblPHIM (MA_PHIM, TEN_PHIM, MA_THE_LOAI, NGAY_PHAT_HANH, HANG_SAN_XUAT) VALUES ('PH7', 'Romantic Comedy', 1, '2005-09-20', 'PQR Films');
INSERT INTO tblPHIM (MA_PHIM, TEN_PHIM, MA_THE_LOAI, NGAY_PHAT_HANH, HANG_SAN_XUAT) VALUES ('PH8', 'Sci-Fi Adventure', 2, '2012-06-16', 'STU Entertainment');
INSERT INTO tblPHIM (MA_PHIM, TEN_PHIM, MA_THE_LOAI, NGAY_PHAT_HANH, HANG_SAN_XUAT) VALUES ('PH9', 'Drama Masterpiece', 3, '2017-02-03', 'VWX Studios');
INSERT INTO tblPHIM (MA_PHIM, TEN_PHIM, MA_THE_LOAI, NGAY_PHAT_HANH, HANG_SAN_XUAT) VALUES ('PH10', 'Horror Flick', 1, '2014-10-29', 'YZA Pictures');

-- Tạo dữ liệu cho bảng LỊCH CHIẾU
INSERT INTO tblLC (MA_LICH, MA_RAP, MA_PHIM, THOI_GIAN, SO_LUONG_VE) VALUES (1, 'B1', 'PH2', '2024-02-15', 135);
INSERT INTO tblLC (MA_LICH, MA_RAP, MA_PHIM, THOI_GIAN, SO_LUONG_VE) VALUES (2, 'B2', 'PH3', '2024-02-18', 140);
INSERT INTO tblLC (MA_LICH, MA_RAP, MA_PHIM, THOI_GIAN, SO_LUONG_VE) VALUES (3, 'B3', 'PH4', '2024-02-21', 145);
INSERT INTO tblLC (MA_LICH, MA_RAP, MA_PHIM, THOI_GIAN, SO_LUONG_VE) VALUES (4, 'B4', 'PH5', '2024-02-24', 150);
INSERT INTO tblLC (MA_LICH, MA_RAP, MA_PHIM, THOI_GIAN, SO_LUONG_VE) VALUES (5, 'B5', 'PH6', '2024-02-27', 155);
INSERT INTO tblLC (MA_LICH, MA_RAP, MA_PHIM, THOI_GIAN, SO_LUONG_VE) VALUES (6, 'C1', 'PH7', '2024-03-01', 130);
INSERT INTO tblLC (MA_LICH, MA_RAP, MA_PHIM, THOI_GIAN, SO_LUONG_VE) VALUES (7, 'C2', 'PH8', '2024-03-04', 135);
INSERT INTO tblLC (MA_LICH, MA_RAP, MA_PHIM, THOI_GIAN, SO_LUONG_VE) VALUES (8, 'C3', 'PH9', '2024-03-07', 140);
INSERT INTO tblLC (MA_LICH, MA_RAP, MA_PHIM, THOI_GIAN, SO_LUONG_VE) VALUES (9, 'C4', 'PH10', '2024-03-10', 145);
INSERT INTO tblLC (MA_LICH, MA_RAP, MA_PHIM, THOI_GIAN, SO_LUONG_VE) VALUES (10, 'C5', 'PH11', '2024-03-13', 150);

-- Thực hành các câu lệnh truy vấn
go
-- Lấy tất cả dữ liệu từ 1 bảng
select * from tblPHIM
-- Lấy thông tin rạp MegaStar
SELECT * from tblRAP where TEN_RAP = 'MegaStar'
go
-- Xóa thông tin phim Sex Is Zero
delete from tblPHIM where TEN_PHIM = 'Sex Is Zero'
select * from tblPHIM
go
-- Cập nhật thông tin phim Xác Ướp Ai Cập thành Cướp Biển Carribe
update tblPHIM set TEN_PHIM = 'Cướp Biển Carribe' where TEN_PHIM = 'Xác Ướp Ai Cập';
select * from tblPHIM
go

gh