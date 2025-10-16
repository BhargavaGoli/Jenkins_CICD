# Minimal FastAPI app for DevOps CI/CD practice
from fastapi import FastAPI, Response

app = FastAPI()

HTML = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>CI/CD Success</title>
    <style>
        body {
            background: linear-gradient(135deg, #00c3ff 0%, #ffff1c 100%);
            min-height: 100vh;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Segoe UI', Arial, sans-serif;
        }
        .card {
            background: rgba(255,255,255,0.95);
            border-radius: 24px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            padding: 48px 36px;
            text-align: center;
            max-width: 400px;
        }
        h1 {
            color: #0f2027;
            font-size: 2.2rem;
            margin-bottom: 0.5em;
        }
        p {
            color: #2d2d2d;
            font-size: 1.2rem;
        }
        .success {
            color: #00b894;
            font-size: 1.5rem;
            font-weight: bold;
            margin-top: 1em;
        }
    </style>
</head>
<body>
    <div class='card'>
        <h1>🎉 Bhargava successfully completed CI-CD pipeline! 🎉</h1>
        
    </div>
</body>
</html>
"""

@app.get("/", response_class=Response)
def read_root():
    return Response(content=HTML, media_type="text/html")
