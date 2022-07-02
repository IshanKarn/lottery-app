from flask import Flask, render_template, request, redirect, url_for, flash
from forms import ParticipantForm
import sqlite3 as sql

app = Flask(__name__)

app.secret_key = 'dev key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/participate', methods=['GET', 'POST'])
def register():
    form = ParticipantForm(request.form)

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required!')
            return render_template('register.html', form=form)
        else:
            return render_template('success.html')
    else:
        return render_template('register.html', form=form)

@app.route('/addrec', methods=['GET', 'POST'])
def addrec():
    if request.method == 'POST':
        try:
            fname = request.form['fname']
            lname = request.form['lname']
            address = request.form['address']
            phone = request.form['phone']
            email = request.form['email']
        
            with sql.connect('database.db') as con:
                cur = con.cursor()
    
                cur.execute("INSERT INTO participants(fname, lname, phone, email, address) \
                    VALUES (?,?,?,?,?)", (fname, lname, phone, email, address))

                con.commit()
                msg = "Registration successful"
        except:
            con.rollback()
            msg = "Error in insert operation"
        finally:
            con.close() 
            return render_template('success.html', msg=msg)
    return redirect(url_for('register'))

if __name__ == '__main__':
    app.run(debug=True)