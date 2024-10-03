# การดำเนินการกับสแตก (Stack) (หลักการเข้าหลังออกก่อน - Last In, First Out - LIFO)
stack = []  # สร้างสแตกว่างเปล่า
stack.append(1)  # เพิ่มค่า 1 เข้าไปในสแตก
stack.append(2)  # เพิ่มค่า 2 เข้าไปในสแตก
stack.append(3)  # เพิ่มค่า 3 เข้าไปในสแตก
popped_item = stack.pop()  # เอาค่าล่าสุดที่เพิ่มเข้ามาออกจากสแตก (ในกรณีนี้คือค่า 3)
print("Popped item from stack:", popped_item)  # Output: Popped item from stack: 3 แสดงค่าที่ถูกเอาออกจากสแตก

# การดำเนินการกับคิว (Queue) (หลักการเข้าแรกออกก่อน - First In, First Out - FIFO)
from collections import deque  # นำเข้า deque จาก collections module
queue = deque([1, 2, 3])  # สร้างคิวเริ่มต้นด้วยค่า 1, 2, 3
queue.append(4)  # เพิ่มค่า 4 เข้าไปในคิว
dequeued_item = queue.popleft()  # เอาค่าแรกที่เข้าไปออกจากคิว (ในกรณีนี้คือค่า 1)
print("Dequeued item from queue:", dequeued_item)  # Output: Dequeued item from queue: 1 แสดงค่าที่ถูกเอาออกจากคิว