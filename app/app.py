from flask import Flask
import datetime, platform

app = Flask(__name__)
VERSION = "2.0.0"

@app.route("/")
def index():
    msg = f"Déployé le {datetime.datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}"
    return f"""
    <h1>Application DevOps</h1>
    <p><strong>Version :</strong> {VERSION}</p>
    <p><strong>Message :</strong> {msg}</p>
    <p><strong>Serveur :</strong> {platform.node()}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
