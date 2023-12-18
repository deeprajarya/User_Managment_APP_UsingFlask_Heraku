from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # SQLite for simplicity
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    hobbies = db.Column(db.String(100))




@app.route('/')
def index():
    with app.app_context():
        users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        with app.app_context():
            name = request.form['name']
            phone_number = request.form['phone_number']
            email = request.form['email']
            hobbies = request.form['hobbies']

            new_user = User(name=name, phone_number=phone_number, email=email, hobbies=hobbies)
            db.session.add(new_user)
            db.session.commit()

    return redirect(url_for('index'))




@app.route('/delete/<int:user_id>')
def delete(user_id):
    with app.app_context():
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()

    return redirect(url_for('index'))




@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit(user_id):
    with app.app_context():
        user = User.query.get(user_id)

        if request.method == 'POST':
            user.name = request.form['name']
            user.phone_number = request.form['phone_number']
            user.email = request.form['email']
            user.hobbies = request.form['hobbies']
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('edit.html', user=user)



app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your email provider
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'example@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'password'  # Replace with your email password

mail = Mail(app)



@app.route('/send_email/<int:user_id>')
def send_email(user_id):
    with app.app_context():
        user = User.query.get(user_id)
        send_email_to_user(user)
    
    return redirect(url_for('index'))



def send_email_to_user(user):
    msg = Message('Subject: User Information',
                  sender='deeprajarya11@gmail.com',  #  You can replace with your email
                  recipients=[user.email])
    msg.body = f"Hello {user.name},\n\nYour user information:\nName: {user.name}\nPhone Number: {user.phone_number}\nEmail: {user.email}\nHobbies: {user.hobbies}"
    
    mail.send(msg)





if __name__ == '__main__':
    app.run(debug=True, port=5000)
