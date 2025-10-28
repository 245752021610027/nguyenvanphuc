print("nguyen van phuc")
print("245752021610027")
ds = input("Nhập danh sách các từ: ").split()
max_len = max(len(tu) for tu in ds)
tu_dai_nhat = [tu for tu in ds if len(tu) == max_len]
print("Từ dài nhất:", ', '.join(tu_dai_nhat))
