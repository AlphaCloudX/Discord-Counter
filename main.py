import pyscreenshot as ImageGrab
import pytesseract
import pyautogui
import time
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USERNAME\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Saving as width and height
width, height = pyautogui.size()

print("5 seconds to get ready")
time.sleep(5)

widthOne = int(width * 0.14453125)
widthTwo = int(width * 0.3578125)
heightOne = int(height * 0.815)
heightTwo = int(height * 0.888888889)

while True:
    try:
        # part of the screen
        im = ImageGrab.grab(bbox=(widthOne, heightOne, widthTwo, heightTwo)).save("img.jpg")  # x1, y1 | x2 y2

        # Getting text from image
        text = pytesseract.image_to_string(Image.open("img.jpg")).split()

        print(text)

        if text[0] != "Discord Username":
            val = int(text[-1]) + 1
            pyautogui.write(str(val))
            pyautogui.press('enter')
            time.sleep(3)

        else:
            print("Waiting For New Input")
            time.sleep(0.5)
        
    except Exception as e:
        print(e)
        print("Please send me a msg with the error through discord, I'll try to help and fix it")