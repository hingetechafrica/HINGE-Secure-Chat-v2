"""
HINGE-Secure-Chat v2 - app.py
HINGE TECH - AI Security for Africa
100% OFFLINE - Flask only, no API key

How to run:
1. pip install flask
2. python app.py
3. Open http://localhost:5000 in your browser
"""

from flask import Flask, request, jsonify, send_file
from chatbot import get_response

app = Flask(__name__)
@app.route('/hinge_logo.png')
def serve_logo():
    return send_file('hinge_logo.png', mimetype='image/png')

# ============================================================
# HOMEPAGE - Clean Modern Design
# HINGE TECH Blue: #0A2540, Accent Blue: #1E90FF
# ============================================================

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HINGE AI - AI Security for Africa</title>
<style>
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Arial, sans-serif; }
  body { background: #f0f2f5; color: #222; }

  /* Header */
  .header {
    background: #0A2540;
    color: white;
    padding: 22px 20px;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
  }
  .header h1 { font-size: 24px; letter-spacing: 0.5px; }
  .header h1 span { color: #1E90FF; }
  .header p { margin-top: 6px; opacity: 0.85; font-size: 14px; }

  /* Main Chat Container */
  .container {
    max-width: 750px;
    margin: 20px auto;
    padding: 0 12px;
  }

  /* Chat Box */
  .chat-box {
    background: white;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    overflow: hidden;
  }

  /* Chat History */
  #chat-history {
    height: 480px;
    overflow-y: auto;
    padding: 18px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .msg { max-width: 85%; padding: 12px 14px; border-radius: 14px; line-height: 1.5; font-size: 15px; white-space: pre-wrap; }
  .msg-user { align-self: flex-end; background: #0A2540; color: white; border-bottom-right-radius: 4px; }
  .msg-bot { align-self: flex-start; background: #eef4ff; color: #222; border-bottom-left-radius: 4px; border: 1px solid #dbe6ff; }

  .msg-bot strong { color: #0A2540; }

  /* Quick Buttons */
  .quick {
    display: flex; flex-wrap: wrap; gap: 8px;
    padding: 12px 16px; background: #f8fafc; border-top: 1px solid #eee;
  }
  .quick button {
    border: 1px solid #0A2540; background: white; color: #0A2540;
    padding: 7px 12px; border-radius: 20px; cursor: pointer; font-size: 13px;
  }
  .quick button:hover { background: #0A2540; color: white; }

  /* Input Area */
  .input-area { display: flex; gap: 10px; padding: 14px; background: white; border-top: 1px solid #eee; }
  #user-input {
    flex: 1; padding: 12px 14px; border: 1.5px solid #ddd; border-radius: 25px;
    font-size: 15px; outline: none;
  }
  #user-input:focus { border-color: #1E90FF; }
  #send-btn {
    background: #0A2540; color: white; border: none;
    padding: 12px 22px; border-radius: 25px; cursor: pointer;
    font-size: 15px; font-weight: 600;
  }
  #send-btn:hover { background: #1E90FF; }

  .footer { text-align: center; padding: 14px; font-size: 12px; color: #888; }
  .footer b { color: #0A2540; }

  /* Mobile */
  @media (max-width: 600px) {
    #chat-history { height: 420px; }
    .header h1 { font-size: 20px; }
  }
</style>
</head>
<body>

<div class="header">
 <img src="/hinge_logo.png" alt="HINGE TECH Logo" style="width:70px; height: auto; display: block; margin: 0 auto 8px auto; border-radius: 12px;"> 
  <h1>HINGE <span>AI</span> - AI Security for Africa</h1>
   <p style="font-size: 12px; opacity: 0.8; margin-top: -8px;">by HINGE TECH</p>
  <p>Ask me about keeping your business safe.</p>
</div>

<div class="container">
  <div class="chat-box">
    <div id="chat-history">
      <div class="msg msg-bot">👋 Hello! I'm <b>HINGE AI v2</b> — your offline cybersecurity assistant from HINGE TECH.<br><br>Ask me about phishing, ransomware, WhatsApp security, Zero Trust, SOC, or NDPC Nigeria.<br><br>Try: <i>"How do hackers steal WhatsApp?"</i></div>
    </div>

    <div class="quick">
      <button onclick="quickAsk('What is phishing?')">Phishing</button>
      <button onclick="quickAsk('How do hackers steal WhatsApp?')">WhatsApp Security</button>
      <button onclick="quickAsk('What is ransomware?')">Ransomware</button>
      <button onclick="quickAsk('What is Zero Trust?')">Zero Trust</button>
      <button onclick="quickAsk('Give me small business security checklist')">Small Business Checklist</button>
    </div>

    <div class="input-area">
      <input id="user-input" type="text" placeholder="Type your question... e.g. My phone is hot and battery drains" autocomplete="off" />
      <button id="send-btn" onclick="sendMessage()">Send</button>
    </div>
  </div>
  <div class="footer">Built by <b>HINGE TECH</b> • Building Secure Technology For Africa • 100% Offline • No data leaves your computer</div>
</div>

<script>
  const historyBox = document.getElementById('chat-history');
  const inputBox = document.getElementById('user-input');

  function addMessage(text, type) {
    const div = document.createElement('div');
    div.className = 'msg msg-' + type;
    div.textContent = text;
    historyBox.appendChild(div);
    historyBox.scrollTop = historyBox.scrollHeight;
  }

  async function sendMessage() {
    const text = inputBox.value.trim();
    if (!text) return;
    addMessage(text, 'user');
    inputBox.value = '';

    // Typing indicator
    const typing = document.createElement('div');
    typing.className = 'msg msg-bot';
    typing.textContent = 'HINGE AI is thinking...';
    historyBox.appendChild(typing);
    historyBox.scrollTop = historyBox.scrollHeight;

    try {
      const res = await fetch('/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: text})
      });
      const data = await res.json();
      historyBox.removeChild(typing);
      addMessage(data.reply, 'bot');
    } catch(e) {
      historyBox.removeChild(typing);
      addMessage('Sorry, something went wrong. Please try again.', 'bot');
    }
  }

  function quickAsk(text) {
    inputBox.value = text;
    sendMessage();
  }

  // Send on Enter key
  inputBox.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') sendMessage();
  });
</script>

</body>
</html>
"""

# ============================================================
# ROUTES
# ============================================================

@app.route("/")
def home():
    """Show homepage"""
    return render_template_string(HTML_PAGE)

@app.route("/chat", methods=["POST"])
def chat():
    """Receive user message, return AI reply"""
    data = request.get_json()
    user_message = data.get("message", "")
    # Call the brain from chatbot.py
    reply = get_response(user_message)
    return jsonify({"reply": reply})

# ============================================================
# RUN THE APP
# ============================================================

if __name__ == "__main__":
    print("="*50)
    print("HINGE-Secure-Chat v2 is running!")
    print("Open: http://localhost:5000")
    print("="*50)
    # debug=True shows errors, host 0.0.0.0 lets phone on same WiFi test it
    app.run(host="0.0.0.0", port=5000, debug=True)
