<?php
header('Access-Control-Allow-Origin:*');
$host = "localhost";
$u = "root";
$p = "";
$db = "appbanhang";

$con = new mysqli($host, $u, $p, $db);
$sql = "select * from sanpham where idsanpham = 2";
$kq = $con->query($sql);

while($row[]=$kq->fetch_assoc()){
    $json = json_encode($row);
}
echo '{"products":'.$json.'}';
$con->close();
?>
