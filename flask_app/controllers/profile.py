
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
 
 
@app.route('/profile/<int:id>')
def search(id):
    if 'users_id' in session:
        data = {
            "id" : id
        } 
        return render_template('profile.html',current_user = user.users.get_one({'id': session["users_id"]}),showmypost = post.posts.showmypost(data))
    return redirect('/home')
 

@app.route('/view/<int:id>', methods = ['get'])
def join(id):
    if 'users_id' not in session:
        return redirect('/home')
    data = {
        "id" :id
    }
    return render_template("view.html",current_user = user.users.get_one({'id': session["users_id"]}),trainerspoki = pokemon.Pokemons.showjoin(data))

@app.route('/delete/<int:id>', methods = ['get'])
def delete(id):
    if 'users_id' not in session:
        return redirect('/home')
    data = {
        "id" :id
    }
    post.posts.delete_it(data)
    return redirect(f'/profile/{id}')

@app.route('/edit/<int:id>', methods=['get'])
def get_edit_html(id):
    if 'users_id' not in session:
        return redirect('/home')
    data = {
        "id": id
    }
    return render_template("edit.html",showmypost = post.posts.show_post_by_id(data),current_user = user.users.get_one({'id': session["users_id"]}) )


@app.route('/change_sighting/<int:id>', methods=['POST'])
def edit(id):

	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
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
        "users_id": request.form['user_id'],
		"post" :filename,
        "titleofpost": request.form['titleofpost'],
        "id":request.form['id']
		}
		post.posts.edit(data)
		print(data)
		return render_template('edit.html', filename=filename, imageurl = filename,current_user = user.users.get_one({'id': session["users_id"]}))
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif') 
		return redirect(request.url)

@app.route('/find_poki') 
def findit():
    if 'users_id' in session:
        return render_template('poki.html',current_user = user.users.get_one({'id': session["users_id"]}))
    return redirect('/')


