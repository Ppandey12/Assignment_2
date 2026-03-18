source .venv/bin/activate

# What modules to install
The modules I installed are 
- flask: `pip install Flask`
- flask_sqlalchemy: `pip install Flask-SQLAlchemy`
- Virtualenv: `python3 -m venv .venv`

I also created a .venv folder to store all of the dependencies for this project. I also created a gitignore file to ignore the .venv so it dont push it into github becasue the file is large and not revelent to the code. 

# How to start the Flask server
Starting this project is fairly easy. To start the Flask server, you can run the following command in your terminal:
- 1. first download the code from github and navigate to the project folder in your terminal.
- 2. create a virtual environment by running `python3 -m venv .venv`
- 3. activate the virtual environment by running `source .venv/bin/activate`
- 4. install the dependencies such as flask and flask_sqlalchemy by running `pip install Flask Flask-SQLAlchemy`
- 5. start the Flask server by running `python app.py`

# What URL to start with
Once you have started the Flask server, you can access the application by going to `http://127.0.0.1:8000/` in your web browser. This will take you to the home page of the application where you can navigate to the list and add items pages.
