from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Flask-Migrate
from openai import OpenAI

app = Flask(__name__)

# PostgreSQL configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flaskuser:mysecurepassword123!@db/flask_openai_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize the database
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Initialize OpenAI client
client = OpenAI(api_key='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')

# Define the QuestionAnswer model
class QuestionAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)

# Root endpoint to render the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# /ask endpoint that handles POST requests for AI interaction
@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')

    # Call the OpenAI API for chat completions
    try:
        completion = client.chat.completions.create(
            model="gpt-4",  # or use gpt-3.5-turbo
            messages=[
                {"role": "user", "content": question}
            ]
        )

        # Extract the answer from the response
        answer = completion.choices[0].message.content.strip()

        # Store the question and answer in the database
        new_qa = QuestionAnswer(question=question, answer=answer)
        db.session.add(new_qa)
        db.session.commit()

        return jsonify({"question": question, "answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
