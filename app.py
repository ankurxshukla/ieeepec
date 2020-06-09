from flask import Flask, render_template, request, redirect
from docx import Document
import classify
import PyPDF2

app = Flask(__name__)

# Index
@app.route('/')
def func():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        if(f.filename.split('.')[-1] == 'docx'):
            doc = Document(f)
            text = ""
            for para in doc.paragraphs:
                text += para.text
            return html.replace('#result#', classify.predict(text))
        else:
            pdfReader = PyPDF2.PdfFileReader(f)
            count = pdfReader.numPages
            text = ""
            for i in range(count):
                page = pdfReader.getPage(i)
                text += page.extractText()
            return html.replace('#result#', classify.predict(text))
    else:
        return 'error'

html = """
<!doctype html>
<html>
    <head>
        <title>IEEE PEC Hackathon</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    </head>
    <body>
        <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom box-shadow">
            <h5 class="navbar-brand my-0 mr-md-auto">IEEE PEC Hackathon</h5>
            <nav class="my-2 my-md-0 mr-md-3">
                <a class="p-2 text-dark" href="#">Project Details</a>
                <a class="p-2 text-dark" href="#">Team</a>
                <a href="https://github.com/ankurxshukla/ieeepec"><svg class="ml-2" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8C0 11.54 2.29 14.53 5.47 15.59C5.87 15.66 6.02 15.42 6.02 15.21C6.02 15.02 6.01 14.39 6.01 13.72C4 14.09 3.48 13.23 3.32 12.78C3.23 12.55 2.84 11.84 2.5 11.65C2.22 11.5 1.82 11.13 2.49 11.12C3.12 11.11 3.57 11.7 3.72 11.94C4.44 13.15 5.59 12.81 6.05 12.6C6.12 12.08 6.33 11.73 6.56 11.53C4.78 11.33 2.92 10.64 2.92 7.58C2.92 6.71 3.23 5.99 3.74 5.43C3.66 5.23 3.38 4.41 3.82 3.31C3.82 3.31 4.49 3.1 6.02 4.13C6.66 3.95 7.34 3.86 8.02 3.86C8.7 3.86 9.38 3.95 10.02 4.13C11.55 3.09 12.22 3.31 12.22 3.31C12.66 4.41 12.38 5.23 12.3 5.43C12.81 5.99 13.12 6.7 13.12 7.58C13.12 10.65 11.25 11.33 9.47 11.53C9.76 11.78 10.01 12.26 10.01 13.01C10.01 14.08 10 14.94 10 15.21C10 15.42 10.15 15.67 10.55 15.59C13.71 14.53 16 11.53 16 8C16 3.58 12.42 0 8 0Z"></path></svg></a>
            </nav>
        </div>
        <div style="margin-left: 25%; margin-right: 25%; margin-top: 2%; text-align: center;">
            <h1 class="display-4">Resume Classifier</h1>
            <p class="lead">Using this tool you can accurately classify your resume into various categories.</p>
        </div>
        <div style="margin-left: 25%; margin-right: 25%; margin-top: 5%;">
            <form id="form" class="needs-validation" action="upload_resume" method = "POST" enctype = "multipart/form-data">
                <div class="input-group">
                    <div class="input-group-prepend">
                      <span class="input-group-text" id="upload_title">Upload</span>
                    </div>
                    <div class="custom-file">
                      <input name='file' type="file" class="custom-file-input" id="file"
                        aria-describedby="upload_title">
                      <label class="custom-file-label" for="file">Choose file</label>
                    </div>
                  </div>
            </form>
          </div>
    </body>
    <div style="margin-left: 25%; margin-right: 25%; margin-top: 5%; text-align: center; margin-bottom: 10%;">
        <h2 class="display-5">Predicted Class:</h2>
        <p class="lead">#result#</p>
    </div>
    <script>
        document.getElementById("file").onchange = function() {
            document.getElementById("form").submit();
        };
    </script>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)