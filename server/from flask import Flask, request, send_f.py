from flask import Flask, request, send_file
import os
import os.path
import uuid
app = Flask(__name__)

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        print(request.files)
        print(request.form)
    if(not request.files['file']):
        return "ty debil"
    file = request.files['file']
    filename = file.filename
    name = str(uuid.uuid4())
    extension = filename.split('.')[1]
    name +='.'+extension
    if(file):
        file.save(os.path.join("flask_app/uploads/", name))
        return 'ok'
    if request.method =='GET':
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
        </form>
        '''

@app.route('/get')
def get():
    filename = request.args.get('filename')
    if filename == None:
        return 'invalid file name',401
        # if(not os.path.exists(os.path.join("..","..","flask_app/uploads/", filename))):
        # return "not found", 404
    return send_file(os.path.join("..","..","flask_app/uploads/", filename))

@app.route('/site')
def site():
    return '''<img src='https://ide-68b13ae863ea4638a6cfa9b87a66e370-8080.cs50.ws/get?filename=83700f17-72c0-40c8-b178-cae595396e83.jpg'>'''

@app.route('/docs')
def docs():
    return send_file('./static/docs.html')
app.run(host='0.0.0.0', port=8080)