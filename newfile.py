from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
        <html>
        <head><title>KEVINPROGRAM.COM</title></head>
        <body style="text-align:center; font-family:sans-serif;">
            <h1>Selamat Datang di KEVINPROGRAM.COM 🐵</h1>
            <p>Website percobaan Python Flask milik Kevin!</p>
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Monkey_face.svg" width="200">
        </body>
        </html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
