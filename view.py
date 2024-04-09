from flask import Flask, render_template, request, redirect, url_for
from logic import calculate_result

# ทำให้เว็บสามารถเรนเดอร์ไฟล์รูปภาพ และcssได้
app = Flask(__name__, template_folder='pages', static_url_path='/static')

# แสดงหน้าแรก
@app.route('/')
def home():
    # ดึงผลลัพธ์Result
    result = request.args.get('result', '') 

    return render_template('home.html', result=result)

# สร้างแถว
@app.route('/create', methods=['POST'])
def create():
    # รับค่าจากหน้าเว็บมาเก็บในตัวแปร
    if request.method == 'POST':
        input_text = request.form.get('input', '')  # ใช้ request.form.get() เพื่อรับข้อความภาษาไทย
        # ค่าอื่นๆที่ไม่ได้รับมาจากเว็บ ได้รับมาจากส่วนของไฟล์ logic.py โดยทำงานเมธอท calculate_result(...)
        result = calculate_result(input_text)  # แก้ไขการส่งพารามิเตอร์ให้เป็น input_text
        return redirect(url_for('home', result=result))
    else:
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
