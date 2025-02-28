length = float(input("Nhập chiều dài hình chữ nhật: "))
width = float(input("Nhập chiều rộng hình chữ nhật: "))
chu_vi_hcn = 2 * (length + width)
dien_tich_hcn = length * width

canh1 = float(input("Nhập cạnh thứ nhất của tam giác: "))
canh2 = float(input("Nhập cạnh thứ hai của tam giác: "))
canh3 = float(input("Nhập cạnh thứ ba của tam giác: "))
chieu_cao_tg = float(input("Nhập chiều cao tương ứng: "))
chu_vi_tg = canh1 + canh2 + canh3
dien_tich_tg = 0.5 * canh1 * chieu_cao_tg

ban_kinh = float(input("Nhập bán kính hình tròn: "))
chu_vi_tron = 2 * 3.141592653589793 * ban_kinh
dien_tich_tron = 3.141592653589793 * ban_kinh * ban_kinh

canh_vuong = float(input("Nhập cạnh hình vuông: "))
chu_vi_vuong = 4 * canh_vuong
dien_tich_vuong = canh_vuong * canh_vuong

day1 = float(input("Nhập cạnh đáy thứ nhất của hình thang: "))
day2 = float(input("Nhập cạnh đáy thứ hai của hình thang: "))
canh_ben1 = float(input("Nhập cạnh bên thứ nhất: "))
canh_ben2 = float(input("Nhập cạnh bên thứ hai: "))
chieu_cao_thang = float(input("Nhập chiều cao: "))
chu_vi_thang = day1 + day2 + canh_ben1 + canh_ben2
dien_tich_thang = 0.5 * (day1 + day2) * chieu_cao_thang

print(f"\nHình chữ nhật - Chu vi: {chu_vi_hcn:.2f}, Diện tích: {dien_tich_hcn:.2f}")
print(f"Hình tam giác - Chu vi: {chu_vi_tg:.2f}, Diện tích: {dien_tich_tg:.2f}")
print(f"Hình tròn - Chu vi: {chu_vi_tron:.2f}, Diện tích: {dien_tich_tron:.2f}")
print(f"Hình vuông - Chu vi: {chu_vi_vuong:.2f}, Diện tích: {dien_tich_vuong:.2f}")
print(f"Hình thang - Chu vi: {chu_vi_thang:.2f}, Diện tích: {dien_tich_thang:.2f}")
