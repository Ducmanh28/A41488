# Mục này ghi lại các góp ý của giáo viên:
- Nghiên cứu phần gửi mã otp tới email hoặc sđt
- Thêm phần validate cho mật khẩu: trên 8 ký tự, có 1 ký tự đặc biệt
- Mật khẩu mới khi đổi phải khác mật khẩu cũ 3 lần gần nhất
- Phân quyền cho user
- Kiểm tra biến History trong db
- Sử dụng biến history để lấy ra lịch sử đổi mật khẩu
- Sửa lại hướng đi, bỏ room, chỉ cần hotel. 


# Chức năng của app
- Đăng ký:
  - Nhập thông tin User
  - Mật khẩu phải trên 8 kí tự, có 1 kí tự đặc biệt
  - Xác thực Email qua OTP 
  - Chọn vai trò: 
    - Chỉ có thể chọn hotel_owner: người quản lý khách sạn
    - Customer: Khách hàng
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
- CRUD:
  - Đối với Hotel_Owner: có quyền thêm mới, sửa, xóa, xem các đối tượng như khách sạn, phòng, dịch vụ,...
  - Đối với Customer: chỉ có quyền xem danh sách các đối tượng, có thêm quyền tạo 1 booking mới

# Database
Các bảng hiện có:

![](/Anh/Screenshot_1019.png)

Nội dung bảng Users:

![](/Anh/Screenshot_1020.png)

# Mô tả quy trình đăng ký
Trước tiên, người dùng nhập vào các thông tin cần thiết, lúc này sẽ chưa có OTP.: 

![](/Anh/Screenshot_1023.png)

Sau khi gửi, mã otp sẽ được gửi tới email đã đăng ký, sau khi nhận 

![](/Anh/zalo.jpg)

Nhập OTP và hoàn thành việc đăng ký:

![](/Anh/Screenshot_1024.png)

# Mô tả quy trình lấy lại mật khẩu khi quên mật khẩu
Nhập vào email của tài khoản đã đăng ký, nếu Email đúng sẽ thực hiện gửi otp tới email

![](/Anh/Screenshot_1025.png)

Sau khi có otp, nhập otp, email và mật khẩu mới để đặt lại mật khẩu. Lưu ý: Mật khẩu mới phải khác mật khẩu cũ đã đặt cách đây 3 lần gần nhất!

![](/Anh/Screenshot_1026.png)

# Mô tả quy trình khởi tạo phòng
Chỉ có người chủ của hotel mới có thể tạo được phòng của họ.

Người chủ khách sạn sẽ truy cập vào trang chủ khách sạn mà họ muốn thêm, sửa, xóa phòng.

Sau đó sẽ thực hiện các thao tác với phòng

# Mô tả quy trình tạo booking
Chỉ có khách hàng mới có quyền tạo booking

Người dùng sẽ chọn khu vực mà họ muốn thuê. 

Ứng dụng hiển thị danh sách các khách sạn 

Người dùng chọn loại khách sạn, sau đó chọn loại phòng(1-5 ứng với mức độ phòng từ thấp đén cao)

Sau chọn và thanh toán xong phòng, trạng thái phòng sẽ được để thành *đã có người thuê*

# Mô tả quá trình đổi mật khẩu:
![](/Anh/Screenshot_1028.png)

Khó khăn trong việc xử lý thông tin lấy từ binlog

