from flask import Flask, render_template, request

app = Flask(__name__)

# CAREER DATA
career_data = {
    "Computer Science": {
        "skills": ["Programming", "Algorithms", "Problem Solving"],
        "roles": ["Software Developer", "AI Engineer"],
        "salary": "₹6–25 LPA"
    },
    "Design": {
        "skills": ["Creativity", "UI/UX"],
        "roles": ["UI Designer", "Graphic Designer"],
        "salary": "₹4–15 LPA"
    },
    "Arts": {
        "skills": ["Communication", "Writing"],
        "roles": ["Content Creator", "Writer"],
        "salary": "₹3–10 LPA"
    }
}

# PREDICTION
def predict_career(i, m, c, l):
    if m >= 4 and l >= 4:
        return "Computer Science"
    elif c >= 4:
        return "Design"
    else:
        return "Arts"

@app.route('/')
def home():
    return render_template("index.html")

# FIXED ROUTE (POST + GET)
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'GET':
        return "⚠️ Please fill the quiz first!"

    try:
        i = int(request.form.get('interest', 0))
        m = int(request.form.get('math', 0))
        c = int(request.form.get('creativity', 0))
        l = int(request.form.get('logic', 0))

        result = predict_career(i, m, c, l)
        score = (i + m + c + l) * 5

        info = career_data.get(result, {})

        return render_template("result.html",
                               result=result,
                               score=score,
                               i=i, m=m, c=c, l=l,
                               info=info)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)