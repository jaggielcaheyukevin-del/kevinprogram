from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><title>KEVINPROGRAM.COM</title></head>
    <body style='text-align:center; background-color:#fafafa;'>
        <h1>Selamat datang di KEVINPROGRAM.COM</h1>
        <p>Website buatan Kevin 😎</p>
        <img src='https://upload.wikimedia.org/wikipedia/commons/3/3a/Baby_Monkey_in_India.jpg' width='300'>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()