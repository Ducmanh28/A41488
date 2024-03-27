# Học môn Lập trình ứng dụng di động
Ghi chép lại kiến thức học tập môn Lập trình ứng dụng di động
## Buổi 1: Giới thiệu lập trình Android
### Các loại ứng dụng
**Native app**: java+kotlin

**CrossPlatform**(đa nền tảng): javascript(Reat Native), dart(Flutter)

### Lập trình Native App
res: chứa tài nguyên và layout

java: chứa code java

gradle: chứa các thư viện cần đồng bộ từ server

android manifest.xml: file cấu hình

### Tạo ứng dụng
Lưu ý: Bắt buộc phải có mạng

Yêu cầu: 
- RAM 16GB, Hoặc 8GB + điện thoại Android
- Chip I5 đời 10 trở lên
- Máy Win10 hoặc 11 Tiếng Anh        
- Tên thư mục không có dấu cách, không dùng tiếng Việt
#### Activity(Màn hình)
Gồm 2 thành phần
- File giao diện: xml(nằm trong thư mục layout)
- File code java(kotlin)

==> Ứng dụng Android quản lý bằng các màn hình
#### Tương tác với màn hình
Tạo nút

Khai báo control
```
Textview [tên text];
# Textview text1;

Button [tên nút];
# Button btn1;
```

Ánh xạ các widget từ Layout vào code Java
```
[tên ]
```