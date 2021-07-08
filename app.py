from flask import Flask, json ,jsonify,request
import unity
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///IntroFlask/dbquestion.db'
db = SQLAlchemy(app)

class question(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, number,content):
        self.number = number
        self.content = content

@app.route('/')

@app.route("/body", methods=['Get'])
def get_all():
    rows = unity.questions("Select * from questions")
    data = []
    for row in rows:
        data.append(
            {
                "number": row[0],
                "content": row[1]
            }
        )

    return jsonify({"quiz": data})

@app.route("/options", methods=['Get'])
def get_option():
    rows = unity.questions("Select * from answers_option")
    data = []
    for row in rows:
        data.append(
            {
                "number": row[0],
                "option_key": row[1],
                "option_content": row[2]
            }
        )

    return jsonify({"option": data})

@app.route("/body/add", methods = ['POST'] )
def insert_quiz(conn):
    newNumber = request.form['number']   
    newContent = request.form['content']
    # newNumber = "9"   
    # newContent = "Does Lam Tran handsome ?"
    quiz = question(newNumber,newContent)
    db.session.add(quiz)
    db.session.commit()
    return "Add successful!"

    
if __name__ == "__main__":
    app.run(debug = True)