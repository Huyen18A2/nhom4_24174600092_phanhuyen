import csv
ds_sinhvien = []
def doc_file(ds_sinhvien: list):
    ds_sinhvien.clear()
    with open("ds_sinhvien.csv", mode='r') as open_file:
        csv_reader = csv.DictReader(open_file)
        for item in csv_reader:
            item["nam_hoc"] = int(item["nam_hoc"])
            item["hoc_ky"] = int(item["hoc_ky"])
            item["diem_trung_binh"] = float(item["diem_trung_binh"])
            ds_sinhvien.append(item)

def tim_kiem_sinh_vien(ds_sinhvien, ma_sv=None, ten_sv=None):
    ket_qua = []
    if ma_sv:
        ket_qua = [sv for sv in ds_sinhvien if sv["id"] == ma_sv]
    elif ten_sv:
        ket_qua = [sv for sv in ds_sinhvien if ten_sv.lower() in sv["ten"].lower()]
    
    if ket_qua:
        print("Thông tin sinh viên tìm được:")
        for sv in ket_qua:
            print(f"ID: {sv['id']}, Tên: {sv['ten']}, Năm học: {sv['nam_hoc']}, Học kỳ: {sv['hoc_ky']}, Điểm trung bình: {sv['diem_trung_binh']}")
    else:
        print("Không tìm thấy sinh viên phù hợp.")

doc_file(ds_sinhvien)
while True:
    print("\nTìm kiếm thông tin sinh viên:")
    lua_chon = input("Nhập '1' để tìm theo mã sinh viên, '2' để tìm theo tên sinh viên, hoặc '3' để thoát: ").strip()
    if lua_chon == '1':
        ma_sv = input("Nhập mã sinh viên: ").strip()
        tim_kiem_sinh_vien(ds_sinhvien, ma_sv=ma_sv)
    elif lua_chon == '2':
        ten_sv = input("Nhập tên sinh viên: ").strip()
        tim_kiem_sinh_vien(ds_sinhvien, ten_sv=ten_sv)
    elif lua_chon == '3':
        print("Thoát chương trình")
        break  
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại")
