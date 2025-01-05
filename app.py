from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)
    option1 = db.Column(db.String(100), nullable=False)
    option2 = db.Column(db.String(100), nullable=False)
    option3 = db.Column(db.String(100), nullable=False)
    option4 = db.Column(db.String(100), nullable=False)
    correct_option = db.Column(db.Integer, nullable=False)

# Uygulama başladığında veritabanını oluşturmak için
@app.teardown_appcontext
def create_tables(exc=None):
    db.create_all()

# @app.before_first_request
# def create_tables():
#     db.create_all()

@app.route('/quiz')
def quiz():
    questions = Question.query.all()
    return render_template('quiz.html', questions=questions)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/")
def index():    
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    questions = Question.query.all()

    for i, question in enumerate(questions):
        answer = request.form.get(f'question{i+1}')
        if answer == str(question.correct_option):
            score += 10

    return render_template('quiz.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)

