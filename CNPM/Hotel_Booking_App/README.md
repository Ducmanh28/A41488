# Góp ý của giáo viên
- Thiết kế lại mô hình ứng dụng
- Bỏ Role
- Admin tự thêm khách sạn
- Khách hàng chỉ có thể tạo Booking
- Lưu ý về các dịch vụ đi kèm ví dụ như số người đi, loại phòng
- ĐẶT HỘ, ĐẶT NHIỀU CÙNG 1 LÚC
# Công việc cần làm hàng tuần
## Tuần 6
- Thiết kế lại hướng đi cho ứng dụng
- Thêm database mẫu
- Thiết kế API thanh toán

# Mô tả ứng dụng
Là một ứng dụng đặt phòng khách sạn. Sử dụng ngôn ngữ lập trình Python và cơ sở dữ liệu MySql làm database để thiết kế hệ thống phần back end.

Ứng dụng có các chức năng cơ bản so với một ứng dụng hoàn chỉnh. Các chức năng đó bao gồm:
- Xác thực: 
  - Đăng ký: Cần có mã OTP để xác nhận email!
  - Đăng nhập: Tạo ra khóa JWT để xác thực khi đăng nhập thành công. Khóa này sẽ có khi người dùng đăng nhập và phải có nó để sử dụng app.
  - Quên mật khẩu: Người dùng nhập vào email để lấy mã OTP để đổi mật khẩu
  - Lấy lại mật khẩu: Sử dụng OTP để lấy lại mật khẩu
- Xem:
  - Xem khách sạn: Hiển thị danh sách tất cả khách sạn
  - Tìm kiếm khách sạn: Nhập vào khu vực, ngày nhận phòng và trả phòng để tìm kiếm khách sạn
  - Xem thông tin chi tiết của 1 khách sạn: Hiển thị toàn bộ thông tin của 1 khách sạn
  - Xem thông tin loại phòng: Hiển thị danh sách các loại phòng của 1 khách sạn, các dịch vụ đi kèm theo
  - Xem bảng thông tin các dịch vụ thêm như: đưa đón, ăn sáng, ăn tối,...
  - Xem hóa đơn trước khi thanh toán
- CRUD:
  - Người dùng có thể tạo 1 Hóa đơn: Hóa đơn được tạo bằng các thông tin về khách sạn, loại phòng, dịch vụ kèm theo, ngày nhận và trả phòng mà người dùng đã chọn trước đó
  - Người dùng có thể chỉnh sửa các thông tin hóa đơn của mình
  - Người dùng có thể hủy hóa đơn đó(khi chưa thanh toán)
  - Có thể thêm, thông tin cá nhân, sửa thông tin và xóa thông tin của mình

# Database
Mô hình database của ứng dụng
![](/Anh/Screenshot_1029.png)

![](/Anh/Screenshot_1030.png)

![](/Anh/Screenshot_1031.png)

![](/Anh/Screenshot_1032.png)

# Sơ đồ hoạt động
![](/Anh/Screenshot_1033.png)

Ban đầu người dùng sẽ cần đăng ký, sau đó đăng nhập vào hệ thống. Với token đã được cấp, người dùng thực hiện quy trình như trong ảnh:
- Tìm kiếm khách sạn: Nhập vào khu vực, check_in, check_out
- Chọn khách sạn mà mình muốn
- Chọn loại phòng
- Chọn các dịch vụ thêm
- Xem lại hóa đơn
- Thanh toán trước 70% của hóa đơn(MOMO)
- Thanh toán thành công! Xác nhận đặt phòng!