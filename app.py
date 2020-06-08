from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Index
@app.route('/')
def func():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)