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

@app.route('/message_app')
def message_app(): 
    if 'users_id' in session:
        return render_template('message_app.html',current_user = user.users.get_one({'id': session["users_id"]}), all = room.rooms.all_room())
    return redirect('/home')


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


@app.route('/getintoroom/<int:id>', methods=['get'])
def get_loginpage_html(id): 
    if 'users_id' not in session:
        if 'room_id' not in session: 
            return redirect('/home') 
    data = {
        "id": id
    }
    return render_template("room.html", one = room.rooms.get_one_room(data), all_chat = message.messages.show_all_messages(data),current_user = user.users.get_one({'id': session["users_id"]}))

@app.route('/create_message/<int:message_id>', methods =['post'])
def new_message(message_id):
    if 'users_id' not in session:
        return redirect('/home')
    if not message.messages.validate_message(request.form):
        return redirect('/home')
    data = {
        "id" : message_id
    }
    print(data)
    message.messages.insert_messages(request.form)
    print(request.form)
    return redirect(f"/getintoroom/{message_id}")
 