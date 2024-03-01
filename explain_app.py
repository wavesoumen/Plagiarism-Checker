##################### Libraries.....****************************

from flask import Flask, render_template, request, redirect, url_for, flash
from googlesearch import search
import PyPDF2
import os
from werkzeug.utils import secure_filename

path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads')
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.add_url_rule(
    "/uploads/<name>", endpoint="download_file", build_only=True
)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.config['SECRET_KEY'] = 'super secret key'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


##### Index function:(not for our interested part)****************************

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['text'] != '' and request.files['file'].filename == '':
            word = request.form['text']
            masukan = "word"
            with open('word.txt', 'w', encoding='utf-8') as f:
                f.write(word)
            return redirect(url_for('plagiarism', name=masukan) + "#hasil")
        elif request.files['file'].filename != '' and request.form['text'] == '':
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('plagiarism', name=filename) + "#hasil")
        else:
            flash('Please fill the form')
            return redirect(request.url)
    return render_template("index.html")


#### The core part and The main function for plagiarism checking....****************************

@app.route('/plagiarism/<name>', methods=['GET', 'POST'])
def plagiarism(name):
    domain = "co.id"    ####Initializing a variable for Google search....****************************
    
    #### Variables for storing outputs and plagiarism texts....****************************
    link_output = []
    hasil_plagiarism = []
    hasil_link = []
    hasil_persen = 0
    inputan_mentah = ""
    inputan = []
    filename = ""
    text = ""
    hasil_plagiarism_final = []
    hasil_link_final = []
    
    
    ###URLs those are blocked from being considered in process.****************************
    link_blocked = ["id.linkedin.com", "linkedin.com", "youtube.com", "instagram.com", "facebook.com", "tokopedia.com",
                    "twitter.com", "reddit.com", "bukalapak.com", "shopee.com", "blibli.com"]
    
    
    if request.method == 'POST':
        
        ###Checking any data or file is uploaded or not....****************************
        if request.form['text'] != '' and request.files['file'].filename == '':
            
            ###Saving the submitted texts to the file 'word.txt'...****************************
            word = request.form['text']
            filename += "word"
            with open('word.txt', 'w', encoding='utf-8') as f:
                f.write(word)
        elif request.files['file'].filename != '' and request.form['text'] == '':
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            
            ###Saving the uploaded file to Server...****************************
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

###Extracting the texts from PDF....****************************
                pdfFileObj = open('uploads/{}'.format(filename), 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                num_pages = pdfReader.numPages
                count = 0
                while count < num_pages:
                    pageObj = pdfReader.getPage(count)
                    count += 1
                    text += pageObj.extractText()
        else:
            flash('Please fill the form')
            return redirect(request.url)

        if filename == "word":
            if request.method == 'POST':
                inputan_mentah += request.form['text']
            else:
                f = open("word.txt", "r")
                inputan_mentah += f.read()
            
            
            ###replacing newline characters with spaces and splitting the raw texts.....****************************
            inputan += inputan_mentah.replace("\n", " ").split(". ")
            
###Iterate the loop for each sentences in the input text, construct and perform Google search query for the sentences and append the plagiarized sentences and links.****************************
            for i in range(len(inputan)):
                query = '"' + inputan[i].strip().replace(".", "").replace('"', "'") + '"'
                for j in range(len(list(search(query, tld=domain, num=10, stop=10, pause=2)))):
                    if i != j:
                        continue
                    hasil_plagiarism.append(inputan[i])
                    hasil_link.append(list(search(query, tld=domain, num=10, stop=10, pause=2))[j])
                    
### Filterring the links with the 'link_blocked' list and append the finals.....****************************
            for i in range(len(hasil_plagiarism)):
                for j in range(len(hasil_link)):
                    if i != j:
                        continue
                    while True:
                        for k in range(len(link_blocked)):
                            if link_blocked[k] in hasil_link[j]:
                                break
                        else:
                            hasil_plagiarism_final.append(hasil_plagiarism[i])
                            hasil_link_final.append(hasil_link[j])
                            break
                        break
                    
### Count the percentage of plagiarism with respect to the number of plagiarized sentences and the total number of sententences given.****************************
            count = len(inputan)
            count_hasil = len(hasil_link_final)
            hasil_persen += (count_hasil / count) * 100
            for i in range(len(hasil_link_final)):
                link_output.append(hasil_link_final[i])
                




#################################
##### Perform the same previous logics, but not for the uploaded PDF file.****************************

        else:
            inputan += text.replace("\n", " ").split(". ")
            for i in range(len(inputan)):
                query = '"' + inputan[i].strip().replace(".", "").replace('"', "'") + '"'
                for j in range(len(list(search(query, tld=domain, num=10, stop=10, pause=2)))):
                    if i != j:
                        continue
                    hasil_plagiarism.append(inputan[i])
                    hasil_link.append(list(search(query, tld=domain, num=10, stop=10, pause=2))[j])
            for i in range(len(hasil_plagiarism)):
                for j in range(len(hasil_link)):
                    if i != j:
                        continue
                    while True:
                        for k in range(len(link_blocked)):
                            if link_blocked[k] in hasil_link[j]:
                                break
                        else:
                            hasil_plagiarism_final.append(hasil_plagiarism[i])
                            hasil_link_final.append(hasil_link[j])
                            break
                        break
            count = len(inputan)
            count_hasil = len(hasil_link_final)
            hasil_persen += (count_hasil / count) * 100
            for i in range(len(hasil_link_final)):
                link_output.append(hasil_link_final[i])


############################################
### This code executes when the file uploaded is not named "word".....****************************


    else:
        if name == "word":
            if request.method == 'POST':
                inputan_mentah += request.form['text']
            else:
                f = open("word.txt", "r")
                inputan_mentah += f.read()
            inputan += inputan_mentah.replace("\n", " ").split(". ")
            for i in range(len(inputan)):
                query = '"' + inputan[i].strip().replace(".", "").replace('"', "'") + '"'
                for j in range(len(list(search(query, tld=domain, num=10, stop=10, pause=2)))):
                    if i != j:
                        continue
                    hasil_plagiarism.append(inputan[i])
                    hasil_link.append(list(search(query, tld=domain, num=10, stop=10, pause=2))[j])
            for i in range(len(hasil_plagiarism)):
                for j in range(len(hasil_link)):
                    if i != j:
                        continue
                    while True:
                        for k in range(len(link_blocked)):
                            if link_blocked[k] in hasil_link[j]:
                                break
                        else:
                            hasil_plagiarism_final.append(hasil_plagiarism[i])
                            hasil_link_final.append(hasil_link[j])
                            break
                        break
            count = len(inputan)
            count_hasil = len(hasil_link_final)
            hasil_persen += (count_hasil / count) * 100
            for i in range(len(hasil_link_final)):
                link_output.append(hasil_link_final[i])
                

###This code executes when the file uploaded is not named "word" and it's not a text file. It reads the text content from the uploaded PDF file, performs plagiarism detection, filters out blocked links, calculates the percentage of plagiarism.****************************

        else:
            pdfFileObj = open('uploads/{}'.format(name), 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            num_pages = pdfReader.numPages
            count = 0
            text = ""
            while count < num_pages:
                pageObj = pdfReader.getPage(count)
                count += 1
                text += pageObj.extractText()
            inputan += text.replace("\n", " ").split(". ")
            for i in range(len(inputan)):
                query = '"' + inputan[i].strip().replace(".", "").replace('"', "'") + '"'
                for j in range(len(list(search(query, tld=domain, num=10, stop=10, pause=2)))):
                    if i != j:
                        continue
                    hasil_plagiarism.append(inputan[i])
                    hasil_link.append(list(search(query, tld=domain, num=10, stop=10, pause=2))[j])
            for i in range(len(hasil_plagiarism)):
                for j in range(len(hasil_link)):
                    if i != j:
                        continue
                    while True:
                        for k in range(len(link_blocked)):
                            if link_blocked[k] in hasil_link[j]:
                                break
                        else:
                            hasil_plagiarism_final.append(hasil_plagiarism[i])
                            hasil_link_final.append(hasil_link[j])
                            break
                        break
            count = len(inputan)
            count_hasil = len(hasil_link_final)
            hasil_persen += (count_hasil / count) * 100
            for i in range(len(hasil_link_final)):
                link_output.append(hasil_link_final[i])
                
                
                
### Return a rendered HTML template with the plagiarism percentage and other datas.****************************
    return render_template("index.html", hasil_persen=hasil_persen, data=inputan, hasil_plagiarism=hasil_plagiarism_final,
                           link_output=link_output, hasil_link=hasil_link_final)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
