# Mục này ghi lại các góp ý của giáo viên:
- Nghiên cứu phần gửi mã otp tới email hoặc sđt
- Thêm phần validate cho mật khẩu: trên 8 ký tự, có 1 ký tự đặc biệt
- Mật khẩu mới khi đổi phải khác mật khẩu cũ 3 lần gần nhất
- Phân quyền cho user

# Chức năng của app
- Đăng ký:
  - Nhập thông tin User
  - Mật khẩu phải trên 8 kí tự, có 1 kí tự đặc biệt
  - Xác thực Email qua OTP 
- Đăng nhập:
  - Có thể sử dụng tên đăng nhập hoặc email để đăng nhập
  - Khi đăng nhập thành công sẽ tạo ra 1 access token. Phải có token này thì mới có thể sử dụng các chức năng CRUD
- Quên mật khẩu:
  - Nhập Email --> Kiểm tra email --> Gửi OTP tới Email
- Lấy lại mật khẩu:
  - Nhập email
  - Nhập OTP
  - Nhập mật khẩu mới
    - Mật khẩu mới phải có 8 kí tự, 1 kí tự đặc biệt
    - Mật khẩu mới phải khác các mật khẩu cũ cách đây 3 lần gần nhất 