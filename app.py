yPython
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
 
 
 
 
app = Flask(__name__)
app.secret_key = "Secret Key"
 
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
 
#Creating model table for our CRUD database
class Data(db.Model):
    studentid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    Amount_due = db.Column(db.String(100))
    date = db.Column(db.Integer())
 
 
    def __init__(self, firstname, lastname, Amount_due, date, studentid):
 
        self.firstname = firstname
        self.lastname = lastname
        self.date = date
        self.Amount_due = Amount_due
        self.studentid = studentid
        
 
 
 
 
 
#This is the index route where we are going to
#query on all our student data
@app.route('/')
def Index():
    all_data = Data.query.all()
 
    return render_template("index.html", student = all_data)
 
 
 
#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        date = request.form['date']
        studentid = request.form['studentid']
        Amount_due = request.form['Amount_due']
 
        my_data = Data(studentid,firstname,lastname,date,amountdue)
        db.session.add(my_data)
        db.session.commit()
 
        flash("student Inserted Successfully")
 
        return redirect(url_for('Index'))
 
 
#this is our update route where we are going to update our employee
@app.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('studentid'))
 
        my_data.firstname = request.form['firstname']
        my_data.lastname = request.form['lastname']
        my_data.studentid = request.form['studentid']
        my_data.Amount_due = request.form['Amount_due']
        my_data.date = request.form['date']
 
        db.session.commit()
        flash("student Updated Successfully")
 
        return redirect(url_for('Index'))
 
 
 
 
#This route is for deleting our employee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(studentid)
    db.session.delete(my_data)
    db.session.commit()
    flash("student Deleted Successfully")
 
    return redirect(url_for('Index'))

def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        student_id = request.form['employee_id']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        date = request.form['date']
        Amount_due = request.form['Amount_due']
        employee = EmployeeModel(employee_id=student_id, firstname=firstname,
                                 lastname=lastname, date = date,
                                 Amount_due=Amount_due)
        db.session.add(student)
        db.session.commit()
        return redirect('/data')
 
 
 
 
 
 
if __name__ == "__main__":
    app.run(debug=True)
