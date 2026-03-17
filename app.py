from todo import TodoList
from flask import Flask, render_template, request, redirect, url_for
from datetime import date
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)





todo_list = TodoList()

@app.route("/")
def home():
    return render_template("home.html", todos=todo_list.items)


@app.route("/add", methods=['POST', 'GET'])
def add():
    today = date.today().isoformat()
    if request.method == 'POST':
        todo_list.add(
        priority = int(request.form['priority']),
        done = bool(request.form.get('option1', False)),
        
        due = request.form['due'],
        note = request.form['description']
        )
        return redirect(url_for('home'))
    return render_template("add.html", today=today)
    
@app.route("/done/<item_id>")
def done(item_id):
    print("Clicked ID:", item_id)

    for item in todo_list.items:
        print("Item ID:", item.identifier)
        if str(item.identifier) == str(item_id):
            item.done = True
            break

    return redirect(url_for("home"))




@app.route("/edit/<item_id>", methods=['POST', 'GET'])
def edit(item_id):
    items = None
    for item in todo_list.items:
        if str(item.identifier) == str(item_id):
            items = item
            break

    if items is None:
        return redirect(url_for("home"))

    if request.method == 'POST':
        items.priority = int(request.form["priority"])
        items.done = "option1" in request.form
        items.due = request.form["due"]
        note = request.form["description"]

        if items.note:
            items.note = f"{note}"
        # else:
        #     items.note = f"{note}"
    
        return redirect(url_for("home"))

    return render_template("edit.html", item=items)

if __name__ == "__main__":
    app.run(debug=True)
