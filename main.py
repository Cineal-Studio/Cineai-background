from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# یہ آپ کا CapCut جیسا Frontend ہے
HTML_CODE = """
<!DOCTYPE html>
<html lang="ur">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CineAI Studio v2</title>
<style>
body{background:#0a0a0f;color:white;font-family:sans-serif;margin:0;display:flex;height:100vh;}
.sidebar{width:80px;background:#12121a;display:flex;flex-direction:column;align-items:center;padding:20px 0;gap:30px;border-right:1px solid #222;}
.main{flex:1;display:flex;flex-direction:column;}
.chat-area{flex:1;padding:30px;overflow:auto;}
.input-area{padding:20px;background:#12121a;display:flex;gap:10px;}
input{flex:1;background:#1e1e2f;border:1px solid #3a3a5a;padding:15px;border-radius:12px;color:white;outline:none;}
button{background:linear-gradient(90deg,#8a2be2,#4a00e0);border:none;padding:15px 30px;border-radius:12px;color:white;font-weight:bold;cursor:pointer;}
.right-panel{width:350px;background:#12121a;border-left:1px solid #222;padding:20px;}
.card{background:rgba(255,255,255,0.05);backdrop-filter:blur(10px);border-radius:16px;padding:15px;margin-bottom:15px;border:1px solid rgba(255,255,255,0.1);}
.neon{box-shadow:0 0 20px rgba(138,43,226,0.5);}
</style>
</head>
<body>
<div class="sidebar">
<div style="font-size:30px">🎬</div>
<div>🏠</div><div>📁</div><div>✨</div><div>🎙️</div>
</div>
<div class="main">
<div class="chat-area" id="chat">
<div class="card neon">
<h3>👋 السلام علیکم بھائی!</h3>
<p>2 لائنوں میں اپنا آئیڈیا لکھو، میں پوری کہانی + 3D تصویر + وائس بنا دوں گا۔</p>
</div>
</div>
<div class="input-area">
<input id="prompt" placeholder="مثال: ایک غریب لڑکا جو جادوئی دنیا میں چلا جاتا ہے...">
<button onclick="generate()">Generate Video ✨</button>
</div>
</div>
<div class="right-panel">
<h3>Live Preview</h3>
<div class="card"><p>🖼️ 3D Pixar Images</p><div style="height:100px;background:linear-gradient(45deg,#8a2be2,#00f2ff);border-radius:10px"></div></div>
<div class="card"><p>🎙️ Voice Wave</p><div style="height:40px;background:#222;border-radius:10px;display:flex;align-items:center;gap:3px;padding:0 10px"><div style="width:4px;height:20px;background:#8a2be2"></div><div style="width:4px;height:35px;background:#8a2be2"></div><div style="width:4px;height:15px;background:#8a2be2"></div></div></div>
</div>
<script>
function generate(){
 let p=document.getElementById('prompt').value;
 if(!p) return;
 document.getElementById('chat').innerHTML+=`<div class="card"><b>آپ:</b> ${p}</div><div class="card neon"><b>CineAI:</b> آپ کی کہانی تیار ہو رہی ہے... 500 الفاظ کی سکرپٹ + 4 HD 3D تصویریں + HD وائس... (Backend Connect کریں)</div>`;
}
</script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_CODE

@app.get("/health")
def health():
    return {"status": "CineAI Studio v2 Running!"}
