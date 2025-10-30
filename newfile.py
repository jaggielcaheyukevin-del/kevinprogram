from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <html>
        <head>
            <title>KEVINPROGRAM.COM</title>
            <style>
                body {
                    background-color: #101820;
                    color: white;
                    text-align: center;
                    font-family: Arial;
                }
                h1 {
                    color: #FFD700;
                }
                img {
                    width: 180px;
                    border-radius: 20px;
                    margin: 15px;
                }
            </style>
        </head>
        <body>
            <h1>Selamat Datang di KEVINPROGRAM.COM</h1>
            <p>Website ini dibuat oleh Kevin!</p>
            <div>
                <img src="https://i.imgur.com/E7F1t6R.jpeg" alt="monyet1">
                <img src="https://i.imgur.com/4pL1R4T.jpeg" alt="monyet2">
                <img src="https://i.imgur.com/JgcT1Kq.jpeg" alt="monyet3">
            </div>
        </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
