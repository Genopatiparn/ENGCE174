# กำหนดเซ็ตสองเซ็ต
set1 = {1, 2, 3, 4}  # เซ็ตที่ 1
set2 = {3, 4, 5, 6}  # เซ็ตที่ 2

# การรวมเซ็ต (Union)
union_set = set1 | set2  # ใช้เครื่องหมาย | เพื่อรวมค่าทั้งหมดจากเซ็ตทั้งสอง โดยไม่ซ้ำกัน

# การหาผลรวมร่วมของเซ็ต (Intersection)
intersection_set = set1 & set2  # ใช้เครื่องหมาย & เพื่อหาค่าที่มีร่วมกันในทั้งสองเซ็ต set1 และ set2

# การหาผลต่างของเซ็ต (Difference)
difference_set = set1 - set2  # ใช้เครื่องหมาย - เพื่อหาค่าที่อยู่ในเซ็ตแรกแต่ไม่อยู่ในเซ็ตที่สอง

# การหาผลต่างสมมาตรของเซ็ต (Symmetric Difference)
symmetric_difference_set = set1 ^ set2  # ใช้เครื่องหมาย ^ เพื่อหาค่าที่อยู่ในเซ็ตใดเซ็ตหนึ่ง แต่ไม่อยู่ในทั้งสองเซ็ตพร้อมกัน

print("Union:", union_set)  # Output: Union: {1, 2, 3, 4, 5, 6} แสดงผลการรวมเซ็ต
print("Intersection:", intersection_set)  # Output: Intersection: {3, 4} แสดงผลการหาผลรวมร่วมของเซ็ต
print("Difference:", difference_set)  # Output: Difference: {1, 2} แสดงผลการหาผลต่างของเซ็ต
print("Symmetric Difference:", symmetric_difference_set)  # Output: Symmetric Difference: {1, 2, 5, 6} แสดงผลการหาผลต่างสมมาตรของเซ็ต