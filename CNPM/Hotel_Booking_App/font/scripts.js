const API_URL = "http://127.0.0.1:5000";  // Cập nhật URL phù hợp

// Đăng ký
function register() {
    const data = {
        username: document.getElementById("username").value,
        email: document.getElementById("email").value,
        password: document.getElementById("password").value,
        phone_number: document.getElementById("phone_number").value,
        full_name: document.getElementById("full_name").value,
        citizen_id: document.getElementById("citizen_id").value,
        otp: document.getElementById("otp").value
    };

    fetch(`${API_URL}/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        alert(result.message || result.error);
        if (result.message === "Đăng ký thành công!") {
            window.location.href = "login.html";
        }
    })
    .catch(error => console.error("Lỗi:", error));
}

// Đăng nhập
function login() {
    const data = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value
    };

    fetch(`${API_URL}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        alert(result.message || result.error);
        if (result.access_token) {
            localStorage.setItem("access_token", result.access_token);
            window.location.href = "home.html";
        }
    })
    .catch(error => console.error("Lỗi:", error));
}
