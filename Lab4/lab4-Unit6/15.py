# กำหนดเซ็ตสองเซ็ต
set1 = {1, 2, 3, 4}  # เซ็ตที่ 1
set2 = {3, 4, 5, 6}  # เซ็ตที่ 2

# การเพิ่มองค์ประกอบเข้าไปในเซ็ต
set1.add(5)  # เพิ่มค่า 5 เข้าไปในเซ็ต set1

# การลบองค์ประกอบออกจากเซ็ต
set2.discard(6)  # ลบค่า 6 ออกจากเซ็ต set2

# การตรวจสอบ subset และ superset
print("Is set1 a subset of set2?", set1.issubset(set2))# ตรวจสอบว่า set1 เป็น subset ของ set2 หรือไม่
print("Is set2 a superset of set1?", set2.issuperset(set1))# ตรวจสอบว่า set2 เป็น superset ของ set1 หรือไม่