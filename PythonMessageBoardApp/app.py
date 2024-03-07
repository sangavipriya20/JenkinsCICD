from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configuring the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Home route to display messages
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message_content = request.form['content']
        new_message = Message(content=message_content)
        
        # Add new message to database
        db.session.add(new_message)
        db.session.commit()
        return redirect('/')
    else:
        messages = Message.query.all()
        return render_template('index.html', messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
