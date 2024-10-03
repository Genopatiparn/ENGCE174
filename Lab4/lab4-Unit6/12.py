# สร้างดิกชันนารีของเกรดนักเรียน
grades = {'Alice': 85, 'Bob': 92, 'Charlie': 88, 'David': 95}  # สร้างดิกชันนารีที่มีชื่อและเกรดของนักเรียน

# เข้าถึงค่าโดยใช้คีย์
print("Bob's grade:", grades['Bob'])  # Output: Bob's grade: 92 แสดงผลเกรดของ Bob โดยใช้คีย์ 'Bob'

# เพิ่มรายการใหม่
grades['Eve'] = 90  # เพิ่มรายการใหม่โดยมีคีย์เป็น 'Eve' และค่าเป็น 90

# การวนลูปผ่านคีย์และค่า
for student, grade in grades.items():  # ใช้ .items() เพื่อดึงคู่ของคีย์และค่า
    print(f"{student}: {grade}")  # แสดงผลชื่อและเกรดของนักเรียนแต่ละคน

# ใช้วิธี get() เพื่อหลีกเลี่ยง KeyError
print("Frank's grade:", grades.get('Frank', 'Grade not found'))  # Output: Frank's grade: Grade not found โดยใช้ .get() เพื่อดึงค่า โดยให้ค่าเริ่มต้นเป็น 'Grade not found' หากคีย์ไม่อยู่ในดิกชันนารี