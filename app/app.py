from flask import Flask
import datetime
import platform

app = Flask(__name__)
VERSION = "2.1.0"

@app.route("/")
def index():
    now = datetime.datetime.now().strftime("%d/%m/%Y à %H:%M:%S")
    return f"""
    <html>
    <head><title>App DevOps</title></head>
    <body style="font-family: Arial; text-align: center; margin-top: 100px;">
        <h1>Application DevOps</h1>
        <p><strong>Version :</strong> {VERSION}</p>
        <p><strong>Message :</strong> Déployé le {now}</p>
        <p><strong>Serveur :</strong> {platform.node()}</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
