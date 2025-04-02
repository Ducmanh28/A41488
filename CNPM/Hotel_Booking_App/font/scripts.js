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
    const usernameOrEmail = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Kiểm tra nếu là email (sử dụng biểu thức chính quy để kiểm tra email)
    const isEmail = /\S+@\S+\.\S+/.test(usernameOrEmail);

    const data = {
        [isEmail ? 'email' : 'username']: usernameOrEmail,
        password: password
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
            localStorage.setItem('customer_id', result.customer_id);
            window.location.href = "home1.html";
        }
    })
    .catch(error => console.error("Lỗi:", error));
}

async function fetchHotels() {
    try {
        let response = await fetch("http://127.0.0.1:5000/hotels");
        let hotels = await response.json();

        let hotelList = document.getElementById("hotel-list");
        hotelList.innerHTML = ""; 

        hotels.forEach(hotel => {
            let hotelCard = `
                <div class="col-md-4">
                    <div class="card hotel-card">
                        <div class="card-body">
                            <h5 class="card-title">${hotel.name}</h5>
                            <p class="card-text">📍 Địa chỉ: ${hotel.address}</p>
                            <p class="card-text">⭐ Đánh giá: ${hotel.rate} sao</p>
                            <p class="card-text">📞 Hotline: ${hotel.hotline}</p>
                            <p class="card-text">🏨 Trạng thái: ${hotel.status}</p>
                        </div>
                    </div>
                </div>
            `;
            hotelList.innerHTML += hotelCard;
        });
    } catch (error) {
        console.error("Lỗi khi tải danh sách khách sạn:", error);
    }
}
fetchHotels();