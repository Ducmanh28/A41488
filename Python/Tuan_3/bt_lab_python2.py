file_name = input("Enter file name: ")
f = open(file_name, 'w')
f.write("Hello both Tony and Hai")
for i in range(1,5,1):
    f.write(f"\r \nTony say hello!{i}")
for j in range(1,6,1):
    f.write(f"\r \nHello {j} Hai")
f.close()

count_1 = 0
count_2 = 0
f = open(file_name,'r')
data = f.readlines()

for i in data:
    print(i)
    if i.startswith("Tony"):
        count_1 += 1
    if i.endswith("Hai"):
        count_2 += 1
print("Số dòng có nội dung bắt đầu bằng chuỗi “Tony”: ",count_1)
print("Số dòng có nội dung kết thúc bằng chuỗi “Hai”: ",count_2)
f.close()
