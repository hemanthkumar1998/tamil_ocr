from flask import Flask,render_template,request
import os
import cv2
import pytesseract
app=Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route('/')
def hi():
    return render_template("browse.html")
@app.route('/upload',methods=['POST'])
def upload():
    if request.method == 'POST':
        target=os.path.join(APP_ROOT,'static/')
        # print(target)
        
        if not os.path.isdir(target):
            os.mkdir(target)
        # text=[]
        filename=""
        destination=""
        fileslist=request.files.getlist("myfile") 
        print(fileslist)
        for file in fileslist:
           
            filename=file.filename
            destination = ''.join([target,filename])
            print("printing destination")
            print(destination)
            file.save(destination)
        img=cv2.imread(destination)
        text=pytesseract.image_to_string(img,lang='tam')
            # text.append(temp)
        os.remove(destination)
        return render_template("display-image.html",data=text)
    else:
        return "GET mthod"

if __name__=='__main__':
    app.run(port=4000)