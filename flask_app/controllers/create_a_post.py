
from flask_app import app
from flask import render_template,request, redirect,session,flash,url_for
from flask_app.models import user
from flask_app.models import message
from flask_app.models import room
from flask_app.models import post 
from flask_app.models import likes
from flask_app.models import pokemon
from datetime import datetime
from flask_bcrypt import Bcrypt
import base64
bcrypt = Bcrypt(app) 
dateFormat = "%m/%d/%Y %I:%M %p"
import os
import urllib.request

from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/create_a_new_post')
def new_post(): 
    if 'users_id' in session:
        return render_template('post.html',current_user = user.users.get_one({'id': session["users_id"]}),all_pokemon=pokemon.Pokemons.show_all_pokemon())
    return redirect('/home')

@app.route('/posts', methods=['POST'])
def upload_image():

	if 'file' not in request.files: 
		flash('No file part')
	if not post.posts.validate_post(request.form):
	
		return redirect('/create_a_new_post')
	file = request.files['file']
	if file.filename == '': 
		flash('No image selected for uploading')
		return redirect(request.url) 
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename) 
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		print(file.filename)
		print('upload_image filename: ' + filename)
		flash('Image successfully uploaded and displayed below')
		data = {
        "users_id": request.form['users_id'], 
		"post" :filename,
        "titleofpost": request.form['titleofpost'],
        "pokemon_id":request.form['pokemon_id']
		}
		post.posts.insert_post(data)
		print(file.filename, "this is the file name")
	
		return render_template('post.html', filename=filename, imageurl = filename,current_user = user.users.get_one({'id': session["users_id"]}))
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif') 
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)