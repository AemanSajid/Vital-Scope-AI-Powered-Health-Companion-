import streamlit.components.v1 as components

def load_chatbot_ui():
    components.html("""
    <style>
    .chat-button {
      position: fixed;
      bottom: 250px; /* Adjusted: Moved significantly higher from the bottom */
      right: 30px;
      z-index: 1000;
      background-color: #d90429;
      color: white;
      border: none;
      border-radius: 50%;
      width: 60px;
      height: 60px;
      font-size: 28px;
      cursor: pointer;
      box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .chat-popup {
      position: fixed;
      bottom: 200px; /* Adjusted: Moved significantly higher to appear above the button */
      right: 30px;
      z-index: 1001;
      background-color: #fff;
      border: 1px solid #ddd;
      border-radius: 10px;
      width: 300px;
      max-height: 400px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.2);
      display: none;
      flex-direction: column;
    }
    .chat-popup-header {
      background-color: #d90429;
      color: white;
      padding: 10px;
      border-top-left-radius: 10px;
      border-top-right-radius: 10px;
      font-weight: bold;
      text-align: center;
    }
    .chat-popup-body {
      padding: 10px;
      overflow-y: auto;
      flex-grow: 1;
      font-size: 14px;
    }
    .chat-popup-input {
      display: flex;
      padding: 10px;
      border-top: 1px solid #ddd;
    }
    .chat-popup-input input {
      flex-grow: 1;
      padding: 5px;
    }
    .chat-popup-input button {
      background-color: #d90429;
      color: white;
      border: none;
      padding: 6px 10px;
      margin-left: 5px;
      cursor: pointer;
    }
    </style>

    <button class="chat-button" onclick="toggleChat()">❤️</button>
    <div class="chat-popup" id="chatPopup">
      <div class="chat-popup-header">Health Bot</div>
      <div class="chat-popup-body" id="chatBody"></div>
      <div class="chat-popup-input">
        <input type="text" id="chatInput" placeholder="Ask a question..." />
        <button onclick="sendChat()">Send</button>
      </div>
    </div>

    <script>
    function toggleChat() {
      const chat = document.getElementById("chatPopup");
      chat.style.display = (chat.style.display === "flex") ? "none" : "flex";
    }

    function sendChat() {
      const input = document.getElementById("chatInput");
      const body = document.getElementById("chatBody");
      const question = input.value.trim();
      if (!question) return;

      body.innerHTML += `<div><b>You:</b> ${question}</div>`;
      input.value = "";

      fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question })
      })
      .then(res => res.json())
      .then(data => {
        body.innerHTML += `<div><b>Cardia:</b> ${data.answer}</div>`;
        data.related.forEach(r => {
          body.innerHTML += `<div style='margin-left:10px;'>- ${r}</div>`;
        });
        body.scrollTop = body.scrollHeight;
      })
      .catch(() => {
        body.innerHTML += `<div><b>Cardia:</b> ❌ Failed to connect to chatbot server.</div>`;
      });
    }
    </script>
    """, height=500) 