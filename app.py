from flask import Flask, render_template, request
import ollama
import mysql.connector
from datetime import datetime

app = Flask(__name__)

db_config = {
    'host':'localhost',
    'user':'root',
    'password':'',
    'database':'navadisha'
}

def get_ai_help(user_problem):
    prompt = f"""
    You are NavaDisha AI, an expert legal aid assistant for rural India. 
    Analyze this user crisis: "{user_problem}"
    Provide a quick solution in this EXACT format:
    PROMPT ANALYSIS: Match this to UN SDG Goal 16 explaining impact on justice access.
    YOUR LEGAL RIGHTS: State 1 specific legal right or constitutional framework.
    GOVERNMENT SCHEMES & ACTION STEPS: 
    - Mention 1 relevant statutory scheme (NALSA/SALSA/etc).
    - Give 1 immediate next step they must take today.
    Keep response under 5 sentences. India context only.
    """
    try:
        response = ollama.generate(model='gemma2:2b', prompt=prompt, options={"num_predict": 120, "temperature": 0.3})
        return response['response']
    except Exception as e:
        return "Legal aid services are currently busy. Please contact your nearest NALSA legal clinic for urgent assistance."


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-help", methods=["POST"])
def get_help():
    user_problem = request.form.get("problem") 
    ai_response = get_ai_help(user_problem)
    
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_query = "INSERT INTO queries (timestamp, problem, track, response) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql_query, (current_time, user_problem, "Track 06", ai_response))
        conn.commit()
        conn.close()
    except Exception as db_err:
        print(f" [Database skipped]: {db_err}")
        
    return render_template("result.html", problem=user_problem, response=ai_response)

if __name__ == "__main__":
    app.run(debug=True)