from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)

# MySQL konfiguráció
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'recipe_app'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingredients = request.form.get('ingredients').split(',')
        cur = mysql.get_db().cursor()
        query = "SELECT name, preparation_time, recipe FROM recipes WHERE ingredients LIKE %s"
        recipes = []
        for ingredient in ingredients:
            cur.execute(query, (f'%{ingredient.strip()}%',))
            recipes.extend(cur.fetchall())
        return render_template('index.html', recipes=recipes)
    return render_template('index.html', recipes=[])

if __name__ == '__main__':
    app.run(debug=True)
