# กำหนดเซ็ตสองเซ็ต
set1 = {1, 2, 3, 4, 5}  # เซ็ตที่ 1
set2 = {3, 4, 5, 6, 7}  # เซ็ตที่ 2

# การรวมเซ็ต (Union)
union_set = set1 | set2  # ใช้เครื่องหมาย | เพื่อรวมค่าทั้งหมดจากเซ็ต set1 และ set2 โดยไม่ซ้ำกัน
print("Union set:", union_set)  # Output: Union set: {1, 2, 3, 4, 5, 6, 7} แสดงผลการรวมเซ็ต

# การหาผลรวมร่วมของเซ็ต (Intersection)
intersection_set = set1 & set2  # ใช้เครื่องหมาย & เพื่อหาค่าที่มีร่วมกันในเซ็ตทั้งสอง
print("Intersection set:", intersection_set)  # Output: Intersection set: {3, 4, 5} แสดงผลการหาผลรวมร่วมของเซ็ต

# การหาผลต่างของเซ็ต (Difference)
difference_set = set1 - set2  # ใช้เครื่องหมาย - เพื่อหาค่าที่อยู่ในเซ็ตแรกแต่ไม่อยู่ในเซ็ตที่สอง
print("Difference set (set1 - set2):", difference_set)  # Output: Difference set (set1 - set2): {1, 2} แสดงผลการหาผลต่างของเซ็ต

# การหาผลต่างสมมาตรของเซ็ต (Symmetric Difference)
symmetric_difference_set = set1 ^ set2  # ใช้เครื่องหมาย ^ เพื่อหาค่าที่อยู่ในเซ็ตใดเซ็ตหนึ่ง แต่ไม่อยู่ในทั้งสองเซ็ตพร้อมกัน
print("Symmetric difference set:", symmetric_difference_set)  # Output: Symmetric difference set: {1, 2, 6, 7} แสดงผลการหาผลต่างสมมาตรของเซ็ต