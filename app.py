from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
from flask import Flask, redirect, render_template, request
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:musthaq@localhost/customer_rating'

db = SQLAlchemy(app)
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer,primary_key = True)
    customer_name = db.Column(db.String(200))
    dealer_name = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())
    
    def __init__(self, customer_name, dealer_name, rating, comments):
        self.customer_name = customer_name
        self.dealer_name = dealer_name
        self.rating = rating
        self.comments = comments
    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods = ['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comment = request.form['comments']
        
        if customer == '' or dealer == '':
            return render_template('home.html', message = "Please fill required details")
        
        if db.session.query(Feedback).filter(Feedback.customer_name==customer).count() == 0:
            data = Feedback(customer, dealer,rating, comment)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, dealer, rating, comment)
            return render_template('success.html')
        return render_template('home.html', message = "You have already filled")
        
if __name__ == '__main__':
    app.run(debug=True)