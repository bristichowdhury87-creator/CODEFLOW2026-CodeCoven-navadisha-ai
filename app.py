from flask import Flask, render_template, request
import mysql.connector
from datetime import datetime
from rag import build_chain, ask_question
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Load RAG chain once on startup
print("Loading RAG pipeline...")
chain = build_chain()
print("RAG ready!")

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'navadisha123',
    'database': 'navadisha'
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-help", methods=["POST"])
def get_help():
    user_problem = request.form.get("problem")
    
    # Use RAG pipeline instead of direct Ollama call
    result = ask_question(chain, user_problem)
    ai_response = result["answer"]

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_query = "INSERT INTO queries (timestamp, problem, track, response) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql_query, (current_time, user_problem, "Track 06", ai_response))
        conn.commit()
        conn.close()
    except Exception as db_err:
        print(f"[Database skipped]: {db_err}")

    return render_template("result.html", problem=user_problem, response=ai_response)

if __name__ == "__main__":
    app.run(debug=True)