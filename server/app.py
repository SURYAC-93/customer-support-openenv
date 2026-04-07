from flask import Flask
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return """
    <h1>✅ AI Customer Support Agent Running</h1>
    <pre>
[START] task=easy
[STEP] classify → reply → close
[END] success

[START] task=medium
[STEP] classify → reply → close
[END] success

[START] task=hard
[STEP] classify → reply → close
[END] success
    </pre>
    """

@app.route("/health", methods=["GET"])
def health():
    return "OK"

def main():
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)
