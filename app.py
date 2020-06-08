from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Index
@app.route('/')
def func():
    return render_template('index.html')

@app.route('/upload_resume', methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return f.filename

if __name__ == "__main__":
    app.run(debug=True)