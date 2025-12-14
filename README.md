<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ShadowHunt+</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600&family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">

    <style>
        * { box-sizing: border-box; }

        body {
            margin: 0;
            min-height: 100vh;
            background: radial-gradient(circle at top, #020617, #000000 70%);
            color: #e5e7eb;
            font-family: 'Poppins', sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .container {
            width: 90%;
            max-width: 520px;
            padding: 35px;
            border-radius: 18px;
            background: rgba(2, 6, 23, 0.9);
            box-shadow: 0 0 25px rgba(56, 189, 248, 0.15), inset 0 0 30px rgba(56, 189, 248, 0.05);
            border: 1px solid rgba(56, 189, 248, 0.25);
            backdrop-filter: blur(12px);
        }

        h1 {
            font-family: 'Orbitron', sans-serif;
            margin-bottom: 5px;
            color: #38bdf8;
            letter-spacing: 1px;
        }

        .subtitle {
            font-size: 14px;
            color: #94a3b8;
            margin-bottom: 25px;
        }

        input {
            width: 100%;
            padding: 14px;
            border-radius: 10px;
            border: 1px solid #1e293b;
            background: #020617;
            color: #e5e7eb;
            outline: none;
            font-size: 15px;
        }

        input::placeholder { color: #64748b; }

        button {
            width: 100%;
            margin-top: 18px;
            padding: 14px;
            border-radius: 12px;
            border: none;
            background: linear-gradient(135deg, #38bdf8, #0ea5e9);
            color: #020617;
            font-weight: 600;
            font-size: 15px;
            cursor: pointer;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            box-shadow: 0 8px 20px rgba(56, 189, 248, 0.35);
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 30px rgba(56, 189, 248, 0.55);
        }

        .result-box {
            margin-top: 25px;
            padding: 18px;
            border-radius: 14px;
            background: rgba(2, 6, 23, 0.85);
            border: 1px solid rgba(56, 189, 248, 0.3);
        }

        .url { font-size: 13px; word-break: break-all; color: #94a3b8; margin-bottom: 10px; }
        .safe { color: #22c55e; }
        .suspicious { color: #facc15; }
        .phishing { color: #ef4444; }

        footer {
            margin-top: 20px;
            text-align: center;
            font-size: 12px;
            color: #475569;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>🛡 ShadowHunt+</h1>
    <div class="subtitle">Advanced Phishing Detection System</div>

    <form method="POST" action="/">
        <input type="text" name="url" placeholder="Enter website URL to scan" required>
        <button type="submit">Scan Website</button>
    </form>

    {% if scanned_url %}
    <div class="result-box">
        <div class="url"><b>Scanned URL:</b> {{ scanned_url }}</div>

        <h2 class="{% if 'Safe' in result %}safe{% elif 'Suspicious' in result %}suspicious{% else %}phishing{% endif %}">
            {{ result }}
        </h2>

        <p>Risk Score: <b>{{ score }}</b></p>
    </div>
    {% endif %}

    <footer>
        © ShadowHunt+ | Cybersecurity Project
    </footer>
</div>

</body>
</html>
