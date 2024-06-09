from flask import Flask, render_template

app =  Flask(__name__)


posts =[
    {
    'author':'Shoffy',
    'title':'kiria kong',
    'content':'story',
    'date':'2020-02-12'
     },
    {
    'author':'maran',
    'title':'laurence',
    'content':'poem',
    'date':'2020-12-22'
     }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__== '__main__':
    app.run(debug=True)