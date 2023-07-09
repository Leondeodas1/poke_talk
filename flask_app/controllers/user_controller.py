
from flask_app import app
from flask import render_template,request, redirect,session,flash,url_for
from flask_app.models import user
from flask_app.models import message
from flask_app.models import room
from flask_app.models import post
from flask_app.models import likes
from flask_app.models import pokemon
from flask_app.models import newssdf
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

@app.route('/recentnews/<int:id>')
def newinfo(id):
    if 'users_id' in session:
        data = {
            "id" : id
        }
        return render_template('recentnews.html',current_user = user.users.get_one({'id': session["users_id"]}),shownewsbyid = newssdf.newson.getnews(data))
    return redirect('/')
 

@app.route('/getnews', methods=['POST'])
def process():
    data= {
        "news" : request.form['newstext'],
        "users_id" : request.form['users_id']
    }
    number = data['users_id']
    # result = data['news']
    # print (type(result))
    newssdf.newson.save_news(data)
    return redirect(f'/recentnews/{number}')

# @app.route('/create_room', methods = ['POST'])
# def create_rooms():
#     if 'users_id' not in session:
#         return redirect('/home')
#     if not room.rooms.validate_room(request.form):
#         return redirect('/home')
#     room.rooms.insert_room(request.form) 
#     print(request.form)
#     return redirect('/home')

@app.route('/homepage', methods =['get']) 
def gohome():
    return redirect('/home')
