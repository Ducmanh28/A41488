<?php
include "connect.php";  

$page = isset($_POST['page']) ? (int)$_POST['page'] : null;
$loai = isset($_POST['loai']) ? (int)$_POST['loai'] : null;

if ($page === null || $loai === null) {
    // Trả về thông báo lỗi nếu thiếu tham số
    $response = [
        'success' => false,
        'message' => 'Thiếu tham số page hoặc loai.'
    ];
    echo json_encode($response);
    exit; // Dừng việc thực thi mã
}

$total = 6;
$offset = ($page - 1) * $total;

// Sửa câu truy vấn để đảm bảo đúng cú pháp
$query = 'SELECT * FROM `sanpham` WHERE `idsanpham` = ? LIMIT ?, ?';

// Chuẩn bị câu truy vấn
$stmt = $conn->prepare($query);

// Kiểm tra và bind các biến vào câu truy vấn
if ($stmt) {
    $stmt->bind_param("iii", $loai, $offset, $total);
    // Thực thi câu truy vấn
    $stmt->execute();
    
    // Lấy kết quả
    $data = $stmt->get_result();
    $result = array();
    while ($row = $data->fetch_assoc()) {
        $result[] = $row;
    }
    
    // Đóng câu truy vấn
    $stmt->close();
} else {
    // Xử lý lỗi khi không thể chuẩn bị câu truy vấn
    $result = array();
}

// Kiểm tra kết quả và trả về JSON
if (!empty($result)) {
    $arr = [
        'success' => true,
        'message' => "thanh cong",
        'result' => $result
    ];
} else {
    $arr = [
        'success' => false,
        'message' => "khong thanh cong",
        'result' => $result
    ];
}

echo json_encode($arr);
?>
