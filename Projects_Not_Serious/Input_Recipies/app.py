from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create a database object
conn = sqlite3.connect('recipes.db')

# Create a cursor object
cursor = conn.cursor()

# Create the database if it doesn't exist
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY,
        recipe_name TEXT
    )
    '''
)

# Return the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Add a recipe
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html')

# Get the recipe name and add to the database
@app.route('/recipe_submitted', methods = ['POST'])
def submit_recipe():
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    recipe_name = request.form['recipe_name']
    cursor.execute('INSERT INTO recipes (recipe_name) VALUES (?)', (recipe_name,))
    conn.commit()
    conn.close()
    print(recipe_name)
    return render_template('recipe_submitted.html')

@app.route('/view_recipes')
def view_recipes():
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM recipes')
    rows = cursor.fetchall()
    conn.close()
    return render_template('view_recipes.html', recipes = rows)

# Place all the recipes into a database





if __name__ == '__main__':
    app.run()