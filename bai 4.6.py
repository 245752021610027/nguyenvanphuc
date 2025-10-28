print("nguyen van phuc")
print("245752021610027")
ten_day_du = input("Nhập tên người (họ và tên riêng): ").split()
if len(ten_day_du) == 2:
    ho, ten = ten_day_du
    print("Họ:", ho)
    print("Tên riêng:", ten)
else:
    print("Vui lòng nhập đúng định dạng: họ và tên riêng (1 âm mỗi phần)")
