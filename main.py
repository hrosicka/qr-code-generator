from flask import Flask, render_template, request, send_file, url_for
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_base64 = None
    if request.method == 'POST':
        url = request.form['url']
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img_io = BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)

        # Převod obrázku na base64 pro zobrazení v HTML
        qr_code_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')

    return render_template('index.html', qr_code_base64=qr_code_base64)

if __name__ == '__main__':
    app.run(debug=True)