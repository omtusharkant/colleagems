from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/marksheet')
def marksheet():
    
    return render_template('marksheet.html')

@app.route('/library')
def library():
    
    return render_template('library.html')

@app.route('/Student_info')
def information():
    
    return render_template('student_info.html')

@app.route('/fee')
def fee():
    
    return render_template('fee.html')

if __name__ == '__main__':
    app.run(debug=True)
