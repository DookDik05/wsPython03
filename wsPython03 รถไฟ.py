#โจทย์ข้อที่ 4 รถไฟมาหาแล้วนะอิอิ

#รับค่าตั๋ว
ticket = int(input("ค่าตั๋ว (บาท): "))

#รับค่าจำนวนเงินที่จะจ่าย
pay = int(input("จำนวนที่จะจ่าย (บาท): "))

#คำนวณจำนวนเงินทอน
change = pay - ticket

#คำนวณจำนวนเหรียญที่ต้องทอน
coin_10 = change // 10
change %= 10

coin_5 = change // 5
change %= 5

coin_2 = change // 2
change %= 2

coin_1 = change // 1

#แสดงผลลัพธ์
print(f'ค่าโดยสารทั้งหมด: {ticket} บาท')
print(f'จำนวนเงิน : {pay} บาท')
print("จำนวนเหรียญที่ต้องทอน: ")
print(f'10 บาท: {coin_10} เหรียญ')
print(f'5 บาท: {coin_5} เหรียญ')
print(f'2 บาท: {coin_2} เหรียญ')
print(f'1 บาท: {coin_1} เหรียญ')
