from flask import Flask, render_template, request, redirect
from docx import Document
import classify

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
        doc = Document(f)
        text = ""
        for para in doc.paragraphs:
            text += para.text
    return classify.predict(text)

if __name__ == "__main__":
    app.run(debug=True)