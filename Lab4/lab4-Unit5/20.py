# สร้างรายการตัวเลข
numbers = [1, 2, 3, 4, 5, 3, 6, 7, 3]  # สร้างรายการตัวเลขเริ่มต้นด้วยค่า 1, 2, 3, 4, 5, 3, 6, 7, 3

# กำหนดค่าที่ต้องการลบ
remove_num = 3  # กำหนดค่าที่ต้องการลบออกจากรายการคือ 3

# ลบค่าที่กำหนดออกจากรายการจนกว่าจะไม่มีค่าเหล่านั้นอยู่ในรายการ
while remove_num in numbers:  # วนลูปตราบใดที่ค่า remove_num ยังอยู่ในรายการ numbers
    numbers.remove(remove_num)  # ลบค่า remove_num ออกจากรายการ

# แสดงรายการหลังจากลบค่า remove_num ออกทั้งหมดแล้ว
print("Numbers after removal:", numbers)  # Output: Numbers after removal: [1, 2, 4, 5, 6, 7]  # แสดงผลรายการหลังจากลบค่า remove_num ออกทั้งหมดแล้ว

# แสดงผลรวมของค่าที่เหลือในรายการ
print("Sum of remaining numbers:", sum(numbers))  # Output: Sum of remaining numbers: 25  # แสดงผลรวมของค่าที่เหลือในรายการ