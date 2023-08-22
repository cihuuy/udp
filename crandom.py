import pyautogui
import time
import random

# Rekaman gerakan mouse sebelumnya (ganti dengan rekaman Anda)
recorded_mouse_actions = [
    (100, 200, 0.5),  # Contoh: Gerakan ke koordinat (100, 200) dalam 0.5 detik
    (300, 400, 0.5),
    # ... tambahkan langkah lainnya
]

for i in range(99999999999990):
    random_delay = random.choice([2, 3, 4, 6])
    time.sleep(random_delay)
    
    # Memainkan kembali rekaman gerakan mouse
    for x, y, duration in recorded_mouse_actions:
        pyautogui.moveTo(x, y, duration=duration)
    
    pyautogui.doubleClick()

