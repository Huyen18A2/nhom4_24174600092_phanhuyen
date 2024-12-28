#9.xem ds 10 svien có điểm cao nhất trường và 10 sv có điểm thấp nhất trường
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

def lay_top_sinh_vien(ds_sinhvien, nam_hoc, hoc_ky, so_luong):
    ds_loc = [
        sv for sv in ds_sinhvien
        if sv["nam_hoc"] == nam_hoc and sv["hoc_ky"] == hoc_ky
    ]
    ds_sap_xep = sorted(ds_loc, key=lambda x: x["diem_trung_binh"], reverse=True)
    
    top_cao_nhat = ds_sap_xep[:so_luong]
    top_thap_nhat = sorted(ds_loc, key=lambda x: x["diem_trung_binh"])[:so_luong]

    print("Top 10 sinh viên có điểm trung bình cao nhất:")
    for sv in top_cao_nhat:
        print(sv)

    print("\nTop 10 sinh viên có điểm trung bình thấp nhất:")
    for sv in top_thap_nhat:
        print(sv)

    return top_cao_nhat, top_thap_nhat
doc_file(ds_sinhvien)
nam_hoc = 2023
hoc_ky = 1
so_luong = 10
lay_top_sinh_vien(ds_sinhvien, nam_hoc, hoc_ky, so_luong)
