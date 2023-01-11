
from flask_app import app
from flask import render_template,request, redirect,session,flash,url_for
from flask_app.models import user
from flask_app.models import message
from flask_app.models import room
from flask_app.models import post
from flask_app.models import likes
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


@app.route('/home') 
def dashboard():
    if 'users_id' in session:
       
        return render_template('dashboard.html',current_user = user.users.get_one({'id': session["users_id"]}),allpost = post.posts.show_posts())
    return redirect('/')

@app.route('/viewpost/<int:id>')
def showpostbyid(id):
    if 'users_id' in session:
        data = {
            "id" : id
        }
        return render_template('view.html',current_user = user.users.get_one({'id': session["users_id"]}),showmypost = post.posts.show_post_by_id(data))
    return redirect('/')

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

@app.route('/delete/<int:id>', methods = ['get'])
def delete(id):
    if 'users_id' not in session:
        return redirect('/home')
    data = {
        "id" :id
    }
    post.posts.delete_it(data)
    return redirect(f'/profile/{id}')

@app.route('/message_app')
def message_app(): 
    if 'users_id' in session:
        return render_template('message_app.html',current_user = user.users.get_one({'id': session["users_id"]}), all = room.rooms.all_room())
    return redirect('/home')


@app.route('/profile/<int:id>')
def search(id):
    if 'users_id' in session:
        data = {
            "id" : id
        }
        return render_template('profile.html',current_user = user.users.get_one({'id': session["users_id"]}),showmypost = post.posts.showmypost(data))
    return redirect('/home')

@app.route('/create_a_new_post')
def new_post(): 
    if 'users_id' in session:
        return render_template('post.html',current_user = user.users.get_one({'id': session["users_id"]}))
    return redirect('/home')

@app.route('/news') 
def news():
    if 'users_id' in session:
        return render_template('news.html',current_user = user.users.get_one({'id': session["users_id"]}))
    return redirect('/')


@app.route('/posts', methods=['POST'])
def upload_image():

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
        "titleofpost": request.form['titleofpost']
		}
		post.posts.insert_post(data)
		print(data)
		return render_template('post.html', filename=filename, imageurl = filename,current_user = user.users.get_one({'id': session["users_id"]}))
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif') 
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)
 
@app.route('/create_room', methods = ['POST'])
def insideroom():
    if room.rooms.validate_room(request.form):
        print(request.form['passcode'])
        pc_hash = bcrypt.generate_password_hash(request.form['passcode'])
        print(pc_hash)
        data = {
            'room_name': request.form['room_name'],
            'users_id' : session['users_id'],
            'passcode': pc_hash
            
        }
        print(data)
        session['room_id']=room.rooms.insert_room(data)
        print(session)
        return redirect('/message_app')
    return redirect('/message_app')


# @app.route('/create_room', methods = ['POST'])
# def create_rooms():
#     if 'users_id' not in session:
#         return redirect('/home')
#     if not room.rooms.validate_room(request.form):
#         return redirect('/home') 
#     room.rooms.insert_room(request.form)
#     print(request.form)
#     return redirect('/home')


@app.route('/getintoroom/<int:id>', methods=['get'])
def get_loginpage_html(id):
    if 'users_id' not in session:
        if 'room_id' not in session: 
            return redirect('/home')
    data = {
        "id": id
    }
    return render_template("room.html", one = room.rooms.get_one_room(data), all_chat = message.messages.show_all_messages(data),current_user = user.users.get_one({'id': session["users_id"]}))
 
@app.route('/homepage', methods =['get'])
def gohome():
    return redirect('/home')


@app.route('/create_message', methods =['post'])
def new_message():
    if 'users_id' not in session:
        return redirect('/home')
    if not message.messages.validate_message(request.form):
        return redirect('/home')
    message.messages.insert_messages(request.form)
    print(request.form)
    return redirect("/message_app")