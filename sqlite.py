from flask import Flask, render_template, request
import sqlite3 as sql
# home.html, student.html, list.html, result.html

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            name = request.form['name']
            addr = request.form['addr']
            city = request.form['city']
            pin = request.form['pin']
            
            with sql.connect("database.db") as con:
                cur= con.cursor()
                cur.execute("INSERT INTO students(name, addr, city, pin) VALUES (?,?,?,?)", (name, addr, city, pin))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "Error in insert operation"
        finally:
            return render_template("result.html", msg = msg)
            con.close()

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("SELECT * FROM STUDENTS")
    
    rows = cur.fetchall()
    return render_template("list.html", rows= rows)

if __name__ == '__main__':
    app.run(debug = True)