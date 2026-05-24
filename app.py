from flask import Flask, render_template, request
from database import save_to_db
from rag import build_chain, ask_question
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

print("Loading RAG pipeline...")
chain = build_chain()
print("NavaDisha AI Ready!")

# WHITELIST - only these keywords = valid legal query
LEGAL_KEYWORDS = [
    # English
    'beat', 'hit', 'violence', 'abuse', 'land', 'salary',
    'wage', 'police', 'arrest', 'hospital', 'doctor',
    'ration', 'school', 'caste', 'dowry', 'evict', 'eviction',
    'right', 'help', 'problem', 'complaint', 'job', 'work',
    'money', 'loan', 'bribe', 'corrupt', 'rape', 'harass',
    'threat', 'murder', 'stolen', 'cheat', 'fraud', 'pension',
    'certificate', 'water', 'electricity', 'toilet', 'house',
    'homeless', 'hungry', 'food', 'starving', 'sick', 'ill',
    'medicine', 'treatment', 'pregnant', 'child', 'labour',
    'forced', 'bonded', 'slave', 'discriminat', 'untouchab',
    'forest', 'crop', 'farm', 'farmer', 'insurance', 'denied',
    'refused', 'illegal', 'injustice', 'justice', 'court',
    'fir', 'complaint', 'custody', 'bail', 'jail', 'prison',

    # Bengali
    'মারধর', 'মার', 'মারছে', 'হিংসা', 'নির্যাতন',
    'জমি', 'বেতন', 'মজুরি', 'পুলিশ', 'গ্রেফতার',
    'হাসপাতাল', 'ডাক্তার', 'রেশন', 'স্কুল', 'জাতি',
    'যৌতুক', 'উচ্ছেদ', 'অধিকার', 'সাহায্য', 'সমস্যা',
    'অভিযোগ', 'কাজ', 'টাকা', 'ঋণ', 'ঘুষ', 'দুর্নীতি',
    'ধর্ষণ', 'হুমকি', 'খুন', 'চুরি', 'প্রতারণা',
    'পেনশন', 'সার্টিফিকেট', 'পানি', 'বিদ্যুৎ', 'বাড়ি',
    'ক্ষুধা', 'অসুস্থ', 'ওষুধ', 'চিকিৎসা', 'শিশু',
    'জোরপূর্বক', 'বৈষম্য', 'ফসল', 'কৃষক', 'বিমা',
    'অস্বীকার', 'অবৈধ', 'অন্যায়', 'বিচার', 'এফআইআর',

    # Hindi
    'मार', 'पीट', 'हिंसा', 'दुर्व्यवहार', 'जमीन',
    'वेतन', 'मजदूरी', 'पुलिस', 'गिरफ्तार', 'अस्पताल',
    'डॉक्टर', 'राशन', 'स्कूल', 'जाति', 'दहेज',
    'बेदखल', 'अधिकार', 'मदद', 'समस्या', 'शिकायत',
    'काम', 'पैसा', 'कर्ज', 'रिश्वत', 'भ्रष्टाचार',
    'बलात्कार', 'धमकी', 'हत्या', 'चोरी', 'धोखा',
    'पेंशन', 'प्रमाण', 'पानी', 'बिजली', 'घर',
    'भूख', 'बीमार', 'दवा', 'इलाज', 'बच्चा',
    'जबरदस्ती', 'भेदभाव', 'फसल', 'किसान', 'बीमा',
    'अस्वीकार', 'गैरकानूनी', 'अन्याय', 'न्याय', 'एफआईआर',
]

INVALID_RESPONSES = {
    "Bengali": "আমি শুধুমাত্র গ্রামীণ ভারতের আইনি সমস্যায় সাহায্য করতে পারি। অনুগ্রহ করে আপনার আইনি সমস্যা জানান।",
    "Hindi": "मैं केवल ग्रामीण भारत की कानूनी समस्याओं में मदद कर सकता हूं। कृपया अपनी कानूनी समस्या बताएं।",
    "English": "I can only help with legal problems faced by rural Indians. Please describe your legal issue."
}

def is_valid_query(problem):
    problem_lower = problem.lower()
    return any(keyword in problem_lower for keyword in LEGAL_KEYWORDS)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-help", methods=["POST"])
def get_help():
    user_problem = request.form.get("problem", "").strip()
    language = request.form.get("language", "English")

    print(f"=== DEBUG ===")
    print(f"Language received: {language}")
    print(f"Problem received: {user_problem}")
    print(f"=============")

    if not user_problem or len(user_problem) < 5:
        return render_template("index.html",
                             error="Please provide a valid problem description!")

    # PYTHON LEVEL VALIDATION
    if not is_valid_query(user_problem):
        invalid_msg = INVALID_RESPONSES.get(language, INVALID_RESPONSES["English"])
        return render_template("result.html",
                             problem=user_problem,
                             response=invalid_msg)

    # Valid query - get AI response
    result = ask_question(chain, user_problem, language)
    ai_response = result["answer"]

    citations = "\n\n".join([doc.page_content
                            for doc in result.get("context", [])])
    save_to_db(user_problem, ai_response, citations)

    return render_template("result.html",
                           problem=user_problem,
                           response=ai_response)
    
if __name__ == "__main__":
    app.run(debug=True)