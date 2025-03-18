let userData = {};  // Lưu dữ liệu đăng ký để dùng lại sau khi nhập OTP

function sendRegister() {
    userData = {
        username: document.getElementById("username").value,
        email: document.getElementById("email").value,
        password: document.getElementById("password").value,
        phone_number: document.getElementById("phone").value,
        full_name: document.getElementById("full_name").value,
        citizen_id: document.getElementById("citizen_id").value
    };

    fetch("http://127.0.0.1:5000/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(userData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
            document.getElementById("otpSection").style.display = "block"; // Hiện ô nhập OTP
        } else {
            alert(data.error);
        }
    })
    .catch(error => console.error("Error:", error));
}

function confirmRegister() {
    let otp = document.getElementById("otp").value;
    userData.otp = otp;  // Thêm OTP vào dữ liệu đăng ký

    fetch("http://127.0.0.1:5000/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(userData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert("Đăng ký thành công!");
            window.location.href = "login.html"; // Chuyển hướng đến trang đăng nhập
        } else {
            alert(data.error);
        }
    })
    .catch(error => console.error("Error:", error));
}
