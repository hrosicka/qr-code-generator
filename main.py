from flask import Flask, render_template, request
import qrcode
from io import BytesIO
import base64

# Initialize the Flask application
app = Flask(__name__)

# --- Application Routes ---

@app.route('/', methods=['GET', 'POST'])
def generate_qr_code():
    """
    Handles the main page, displaying the URL input form and generating
    a QR code based on POST requests. The generated image is returned
    as a base64 string for embedding in the HTML template.
    """
    qr_code_base64 = None

    if request.method == 'POST':
        # Retrieve the URL data from the submitted form
        url_data = request.form.get('url')

        if url_data:
            # Configure the QR code parameters
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            # Add data and make it fit the code structure
            qr.add_data(url_data)
            qr.make(fit=True)

            # Create the QR code image with specified colors
            img = qr.make_image(fill_color="black", back_color="white")

            # Save the image to an in-memory byte stream (BytesIO)
            img_io = BytesIO()
            img.save(img_io, 'PNG')
            img_io.seek(0)

            # Encode the image to base64 for direct display in HTML
            qr_code_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')

    # Render the template, passing the base64 string if a QR code was generated
    return render_template('index.html', qr_code_base64=qr_code_base64)

# --- Application Startup ---

if __name__ == '__main__':
    # Setting debug to True is useful for development.
    # Should be set to False in a production environment.
    app.run(debug=True)
