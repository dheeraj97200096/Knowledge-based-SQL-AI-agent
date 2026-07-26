from flask import Flask, request, jsonify, send_from_directory
from query_engine import QueryEngine

app = Flask(__name__, static_folder="static")
engine = QueryEngine()

@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    user_input = data.get("question", "")
    intent = engine.parse_intent(user_input)
    sql = engine.generate_sql(intent)
    return jsonify({"sql": sql})

if __name__ == "__main__":
    app.run(debug=True)
