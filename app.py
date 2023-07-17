import os
from flask import Flask, flash, request, redirect, url_for ,render_template
from werkzeug.utils import secure_filename
import search
from jsonfunction import jsonsave,jsonclear
import textfun
import updatetxt
import pdf
import shutil
from grammar import correct

JSON_FILE_PATH = 'data/data.json'
UPLOAD_FOLDER = './static/images/'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', 'gif','pdf'}
message = ''
oldkeyword=''
notindictonary =[]
temp =False
app = Flask(__name__)
app.secret_key = "abc"  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/find/<keyword>')
def findkeyword(keyword):
    imagelist = search.search_keyword(keyword)
    return render_template('imagesoutput.html' , imagelist = imagelist,message =message,oldkeyword=oldkeyword)

@app.route('/updatedict/<text>')
def updatedict(text):
    updatetxt.update(text)
    return redirect(url_for('home'))

@app.route('/oldkeywordfun')
def oldkeywordfun():
    imagelist = search.search_keyword(oldkeyword)
    return render_template('imagesoutput1.html' , imagelist = imagelist,oldkeyword=oldkeyword)


@app.route('/',methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/search',methods=['GET', 'POST'])
def searchfun():
    if request.method == 'POST':
        global message
        global oldkeyword
        global notindictonary
        message = ''
        keyword = request.form.get('keyword')
        if(keyword==''):
            flash('Enter a keyword')
            return redirect(url_for('home'))
        oldkeyword = keyword
        print(keyword)
        a =correct(keyword)
        spelling =a['correct']
        notindictonary =a['notindictonary']
        print(notindictonary)
        if len(notindictonary) != 0:
            return redirect(url_for('oldkeywordfun'))
        print("hi this is spelling hi hello")
        print(spelling)
        print("hi this is spelling hi hello")
        if(spelling != oldkeyword):
            message= f'Showing results for {spelling}'
            print(message)
            keyword = spelling
        print("this is keyword",keyword)

        return redirect (url_for('findkeyword' ,keyword =keyword))

@app.route('/uploadfile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        # if 'file' not in request.files:
        #     flash('No file part')
        #     return redirect(request.url)
        file = request.files['upload']

        print('k')
        print(file)
        print('k')
        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)
        if file and allowed_file(file.filename):
            extention = file.filename.rsplit('.', 1)[1].lower()
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)  
            if(extention == 'pdf'):
                pdf.pdfconvert(filepath)
            else:    
                text_data = textfun.textfunwithkeyword(filepath)
                jsonsave(filename,text_data)
           
    return render_template('upload.html')

@app.route('/cleardatabase', methods=['GET', 'POST'])
def cleardb():
    
    shutil.rmtree(UPLOAD_FOLDER)
    os.mkdir(UPLOAD_FOLDER)
    jsonclear()
    return redirect(url_for('home'))

app.run()