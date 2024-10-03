# กำหนดรายการสามรายการ
list1 = [1, 2, 3, 4, 5]  # รายการที่ 1
list2 = [3, 4, 5, 6, 7]  # รายการที่ 2
list3 = [5, 6, 7, 8, 9]  # รายการที่ 3

# หาค่าเฉพาะจากหลายรายการ
unique_elements = set(list1).union(set(list2)).difference(set(list3))  # ใช้ union เพื่อรวมค่าใน set ที่แปลงมาจาก list1 และ list2 แล้วใช้ difference เพื่อลบค่าที่มีอยู่ใน set ที่แปลงมาจาก list3

# union(set(list1), set(list2)) จะรวมค่าทั้งหมดจาก list1 และ list2 โดยไม่ซ้ำกัน
# difference(set(list1).union(set(list2)), set(list3)) จะลบค่าที่มีอยู่ใน list3 ออกจากผลลัพธ์ของ union

# แสดงผลค่าเฉพาะที่ไม่ซ้ำกันใน list1 และ list2 แต่ไม่อยู่ใน list3
print("Unique elements:", unique_elements)  # Output: Unique elements: {1, 2}  # แสดงผลค่าเฉพาะที่ไม่ซ้ำกันใน list1 และ list2 แต่ไม่อยู่ใน list3