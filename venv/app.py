from flask import Flask, render_template, redirect, request, flash, url_for
from flask_wtf import FlaskForm
from wtforms import SearchField, SubmitField, FileField
from wtforms.validators import InputRequired
from werkzeug.utils import secure_filename
import os
import pandas as pd


app=Flask(__name__)



#form classes
class SearchForm(FlaskForm):
    obj_to_search=SearchField('What object do you want?')
    submit=SubmitField("Search")

class UploadForm(FlaskForm):
    file_upload=FileField('Upload Video', validators=[InputRequired()])
    submit=SubmitField("Upload File")

app.config['SECRET_KEY']='hard to guess string'
    
app.config['MAX_CONTENT_LENGTH'] = 6 * 1000 * 1000

ALLOWED_EXTENSIONS = set(['mp4', 'avi', '720p', '480p', '360p', 'gif'])
MAIN_DF = pd.read_csv('./video_clips_data.csv')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    search_form=SearchForm()
    set_1_videos=pd.DataFrame(MAIN_DF.iloc[:15]).video_src.tolist()
    return render_template('index.html', search_form=search_form, all_videos=set_1_videos)
@app.route('/set_2')
def set_2():
    search_form=SearchForm()
    set_2_videos=pd.DataFrame(MAIN_DF.iloc[15:30]).video_src.tolist()
    return render_template('index.html', search_form=search_form, all_videos=set_2_videos)
@app.route('/set_3')
def set_3():
    search_form=SearchForm()
    set_3_videos=pd.DataFrame(MAIN_DF.iloc[30:45]).video_src.tolist()
    return render_template('index.html', search_form=search_form, all_videos=set_3_videos)
@app.route('/set_4')
def set_4():
    search_form=SearchForm()
    set_4_videos=pd.DataFrame(MAIN_DF.iloc[45:60]).video_src.tolist()
    return render_template('index.html', search_form=search_form, all_videos=set_4_videos)
@app.route('/set_5')
def set_5():
    search_form=SearchForm()
    set_5_videos=pd.DataFrame(MAIN_DF.iloc[60:75]).video_src.tolist()
    return render_template('index.html', search_form=search_form, all_videos=set_5_videos)
@app.route('/set_6')
def set_6():
    search_form=SearchForm()
    set_6_videos=pd.DataFrame(MAIN_DF.iloc[75:90]).video_src.tolist()
    return render_template('index.html', search_form=search_form, all_videos=set_6_videos)
@app.route('/set_7')
def set_7():
    search_form=SearchForm()
    set_7_videos=pd.DataFrame(MAIN_DF.iloc[90:105]).video_src.tolist()
    return render_template('index.html', search_form=search_form, all_videos=set_7_videos)
@app.route('/set_8')
def set_8():
    search_form=SearchForm()
    set_8_videos=pd.DataFrame(MAIN_DF.iloc[105:120]).video_src.tolist()
    return render_template('index.html', search_form=search_form, all_videos=set_8_videos)
@app.route('/set_9')
def set_9():
    search_form=SearchForm()
    set_9_videos=pd.DataFrame(MAIN_DF.iloc[120:135]).video_src.tolist()
    return render_template('index.html', search_form=search_form, all_videos=set_9_videos)


@app.route('/upload', methods=['POST'])
def upload():
    search_form=SearchForm()
    upload_form=UploadForm()
    set_1_videos=pd.DataFrame(MAIN_DF.iloc[:15])
    msg=''
    if request.method == 'POST':
        file = request.files['file_upload']
        # check if the post request has the file part
        if 'file_upload' not in request.files:
            #flash('No file part')
            msg='No file part'
            return render_template('upload.html', search_form=search_form, upload_form=upload_form, msg=msg)
        elif file.filename == '':
            #flash('No file selected for uploading')
            msg='No file selected for uploading'
            return render_template('upload.html', search_form=search_form, upload_form=upload_form, msg=msg)
        elif file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(file.filename)
            msg='File successfully uploaded'
            return render_template('index.html', search_form=search_form, all_videos=set_1_videos)
        else:
            msg="Allowed file types: mp4, avi, 720p, 480p, 360p , gif"
            return render_template('upload.html', search_form=search_form, upload_form=upload_form, msg=msg)
    return render_template('upload.html', search_form=search_form, upload_form=upload_form,msg=msg)

    
app.add_url_rule('/', 'index', index)
app.add_url_rule('/upload', 'upload', upload)