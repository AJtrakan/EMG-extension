import machine
import time

# กำหนดขา (pin) ที่เซนเซอร์ EMG ต่อกับบอร์ด MicroPython
emg_pin = machine.Pin(14, machine.Pin.IN)  # ตั้งค่าขา GPIO ที่เชื่อมต่อกับเซนเซอร์ EMG

# กำหนดจำนวนของตัวอย่างในการทำ moving average filter
NUM_SAMPLES = 10

# ลิสต์เก็บข้อมูลตัวอย่าง
samples = [0] * NUM_SAMPLES

while True:
    # อ่านค่าจากเซนเซอร์ EMG
    emg_value = emg_pin.value()

    # เพิ่มค่าใหม่เข้าไปในลิสต์
    samples.pop(0)
    samples.append(emg_value)

    # คำนวณค่าเฉลี่ยของตัวอย่างในลิสต์ (moving average)
    emg_filtered = sum(samples) / NUM_SAMPLES

    print("Filtered EMG Value:", emg_filtered)  # แสดงค่า EMG ที่ผ่านการทำฟิวเตอร์
    time.sleep(0.1)  # รอเป็นช่วงๆ 0.1 วินาที ก่อนที่จะอ่านค่า EMG อีกครั้ง