import os
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# خودکار بٹن کلک کرنے کا فنکشن
def click_screen(x, y):
    os.system(f"adb shell input tap {x} {y}")

# خودکار ٹیکسٹ ٹائپ کرنے کا فنکشن
def type_text(text):
    os.system(f"adb shell input text '{text}'")

@app.route('/')
def home():
    return "ADB آٹومیشن سرور آن لائن ہے!"

@app.route('/auto_signup', methods=['GET', 'POST'])
def auto_signup():
    # 1. سکرین پر مخصوص جگہ کلک کرنا (X=500, Y=1000)
    click_screen(500, 1000)
    
    time.sleep(1)
    # 2. خودکار نام ٹائپ کرنا
    type_text("ZeeshanUser")
    
    return jsonify({"status": "کامیاب", "message": "آٹومیشن کمانڈز چلا دی گئی ہیں۔"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
