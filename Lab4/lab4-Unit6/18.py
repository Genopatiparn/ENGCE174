# สร้างดิกชันนารีของเกรดนักเรียน
grades = {'Alice': [85, 90, 92], 'Bob': [88, 87, 85], 'Charlie': [90, 91, 89]}  # ดิกชันนารีที่มีชื่อนักเรียนและรายการเกรดของพวกเขา
average_grades = {}  # สร้างดิกชันนารีว่างเปล่าสำหรับเก็บค่าเกรดเฉลี่ย

# คำนวณเกรดเฉลี่ยของนักเรียนแต่ละคน
for student, grade_list in grades.items():  # วนลูปผ่านนักเรียนแต่ละคนและรายการเกรดของพวกเขา
    average_grades[student] = sum(grade_list) / len(grade_list)  # คำนวณเกรดเฉลี่ยโดยใช้ผลรวมของเกรดหารด้วยจำนวนเกรดและเก็บในดิกชันนารี average_grades

# แสดงเกรดเฉลี่ยของนักเรียนแต่ละคน
print("Average Grades:", average_grades)  # Output: Average Grades: {'Alice': 89.0, 'Bob': 86.66666666666667, 'Charlie': 90.0}
