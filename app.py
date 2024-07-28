from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'YOUR_CLOUD_DB_HOST',
    'user': 'YOUR_CLOUD_DB_USERNAME',
    'password': 'YOUR_CLOUD_DB_PASSWORD',
    'database': 'YOUR_CLOUD_DB_NAME'
}

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    holding_name = request.form['holding_name']
    holding_type = request.form['holding_type']
    shares_held = request.form['shares_held']
    br_participation = request.form['br_participation']
    current_year = request.form['current_year']
    previous_year = request.form['previous_year']
    current_year_complaints = request.form['current_year_complaints']
    previous_year_complaints = request.form['previous_year_complaints']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = ("INSERT INTO company_data (holding_name, holding_type, shares_held, br_participation, current_year, previous_year, current_year_complaints, previous_year_complaints) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    values = (holding_name, holding_type, shares_held, br_participation, current_year, previous_year, current_year_complaints, previous_year_complaints)

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for('form'))

if __name__ == '__main__':
    app.run(debug=True)
