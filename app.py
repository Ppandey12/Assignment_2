from todo import TodoList
from flask import Flask, render_template, request, redirect, url_for
from datetime import date, datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    priority = db.Column(db.Integer)
    done = db.Column(db.Boolean, default=False)
    due = db.Column(db.Date)
    note = db.Column(db.String(200))
    created = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comment', backref='todo', lazy=True)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_id = db.Column(db.Integer, db.ForeignKey('todo.id'), nullable=False)
    text = db.Column(db.String(200))



@app.route("/")
def home():
    todos = Todo.query.all()
    return render_template("home.html", todos=todos)


@app.route("/add", methods=['POST', 'GET'])
def add():
    today = date.today().isoformat()
    if request.method == 'POST':
        due_date = datetime.strptime(request.form['due'], "%Y-%m-%d").date()
        new_todo = Todo(
            priority=int(request.form['priority']),
            done=bool(request.form.get('option1', False)),
            due=due_date,
            note=request.form['description']
        )
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", today=today)



@app.route("/done/<int:item_id>")
def done(item_id):
    todo_item = Todo.query.get(item_id)
    if todo_item:
        todo_item.done = True
        db.session.commit()
    return redirect(url_for("home"))

@app.route("/edit/<item_id>", methods=['POST', 'GET'])
def edit(item_id):
    item = Todo.query.get_or_404(item_id)
    # if item is None:
    #     return redirect(url_for("home"))

    if request.method == 'POST':
        item.priority = int(request.form["priority"])
        item.done = "option1" in request.form
        item.due = datetime.strptime(request.form["due"], '%Y-%m-%d').date()
        item.note = request.form["description"]

    
        new_comment_txt= request.form.get("comment", "").strip()
        if new_comment_txt:
            commen_text = Comment(todo_id=item.id, text=new_comment_txt)
            db.session.add(commen_text)

        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", item=item)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
