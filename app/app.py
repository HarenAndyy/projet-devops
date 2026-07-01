from flask import Flask
import datetime
import platform

app = Flask(__name__)
VERSION = "2.2.0"

@app.route("/")
def index():
    now = datetime.datetime.now().strftime("%d/%m/%Y à %H:%M:%S")
    hostname = platform.node()
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>App DevOps CI/CD</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            background: #0f0f1a;
            color: #fff;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}

        .container {{
            width: 90%;
            max-width: 800px;
        }}

        .header {{
            text-align: center;
            margin-bottom: 40px;
        }}

        .header h1 {{
            font-size: 2.5em;
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 8px;
        }}

        .header p {{
            color: #888;
            font-size: 0.95em;
        }}

        .badge {{
            display: inline-block;
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            color: white;
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: bold;
            margin-top: 8px;
        }}

        .cards {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}

        .card {{
            background: #1a1a2e;
            border: 1px solid #2a2a4a;
            border-radius: 12px;
            padding: 24px;
            text-align: center;
            transition: transform 0.2s;
        }}

        .card:hover {{
            transform: translateY(-4px);
            border-color: #0072ff;
        }}

        .card .icon {{
            font-size: 2em;
            margin-bottom: 12px;
        }}

        .card .label {{
            font-size: 0.8em;
            color: #888;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }}

        .card .value {{
            font-size: 1.1em;
            font-weight: bold;
            color: #e0e0ff;
        }}

        .pipeline {{
            background: #1a1a2e;
            border: 1px solid #2a2a4a;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 30px;
        }}

        .pipeline h2 {{
            font-size: 1em;
            color: #888;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 20px;
        }}

        .steps {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
        }}

        .step {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
        }}

        .step .dot {{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: linear-gradient(135deg, #00c6ff, #0072ff);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.1em;
        }}

        .step .name {{
            font-size: 0.75em;
            color: #aaa;
        }}

        .arrow {{
            color: #0072ff;
            font-size: 1.2em;
            flex: 1;
            text-align: center;
        }}

        .footer {{
            text-align: center;
            color: #444;
            font-size: 0.8em;
        }}

        .status {{
            display: inline-block;
            width: 8px;
            height: 8px;
            background: #00ff88;
            border-radius: 50%;
            margin-right: 6px;
            animation: pulse 2s infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.3; }}
        }}
    </style>
</head>
<body>
    <div class="container">

        <div class="header">
            <h1>🚀 Application DevOps</h1>
            <p>Pipeline CI/CD automatisé</p>
            <div class="badge">v{VERSION}</div>
        </div>

        <div class="cards">
            <div class="card">
                <div class="icon">📦</div>
                <div class="label">Version</div>
                <div class="value">{VERSION}</div>
            </div>
            <div class="card">
                <div class="icon">🕐</div>
                <div class="label">Déployé le</div>
                <div class="value">{now}</div>
            </div>
            <div class="card">
                <div class="icon">🖥️</div>
                <div class="label">Serveur</div>
                <div class="value">{hostname}</div>
            </div>
            <div class="card">
                <div class="icon">⚙️</div>
                <div class="label">Statut</div>
                <div class="value"><span class="status"></span>En ligne</div>
            </div>
        </div>

        <div class="pipeline">
            <h2>Pipeline CI/CD</h2>
            <div class="steps">
                <div class="step">
                    <div class="dot">📁</div>
                    <div class="name">Git</div>
                </div>
                <div class="arrow">→</div>
                <div class="step">
                    <div class="dot">🔧</div>
                    <div class="name">Build</div>
                </div>
                <div class="arrow">→</div>
                <div class="step">
                    <div class="dot">✅</div>
                    <div class="name">Test</div>
                </div>
                <div class="arrow">→</div>
                <div class="step">
                    <div class="dot">🐳</div>
                    <div class="name">Docker</div>
                </div>
                <div class="arrow">→</div>
                <div class="step">
                    <div class="dot">🌐</div>
                    <div class="name">Nginx</div>
                </div>
            </div>
        </div>

        <div class="footer">
            Pipeline automatisé · Git · Jenkins · Docker · Nginx
        </div>
    </div>
</body>
</html>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
