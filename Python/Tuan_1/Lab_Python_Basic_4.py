day1 = int(input("Nhập cạnh đáy thứ nhất của hình thang: "))
day2 = int(input("Nhập cạnh đáy thứ hai của hình thang: "))
canh_ben1 = int(input("Nhập cạnh bên thứ nhất: "))
canh_ben2 = int(input("Nhập cạnh bên thứ hai: "))
chieu_cao_thang = int(input("Nhập chiều cao: "))
chu_vi_thang = day1 + day2 + canh_ben1 + canh_ben2
dien_tich_thang = 0.5 * (day1 + day2) * chieu_cao_thang

print(f"Hình thang - Chu vi: {chu_vi_thang}, Diện tích: {dien_tich_thang}")

so_dollar = float(input("Nhập số Dollar: "))
ty_gia = 23000
so_vnd = so_dollar * ty_gia

print(f"{so_dollar} Dollar tương đương {so_vnd} đồng VN")
