<?php
header('Access-Control-Allow-Origin:*');

$host = "localhost";
$u = "root";
$p = "";
$db = "appbanhang";

$con = new mysqli($host, $u, $p, $db);

if ($con->connect_error) {
    die("Kết nối thất bại: " . $con->connect_error);
}



// $tenKhachHang = "abc dl";
// $soDienThoai = "0383693748";
// $diaChi = "trung van, nam tu liem, ha noi";

$tenKhachHang = $_POST['tenkhachhang'];
$soDienThoai = $_POST['sodienthoai'];
$diaChi = $_POST['diachi'];

$sql = "INSERT INTO donhang (tenkhachhang, sodienthoai, diachi) VALUES ('$tenKhachHang', '$soDienThoai', '$diaChi')";

if ($con->query($sql) === TRUE) {
    echo "Dữ liệu đã được thêm thành công vào bảng donhang";
} else {
    echo "Lỗi: " . $sql . "<br>" . $con->error;
}

$con->close();
?>
