from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mydb = 'poke_social_media'
 
class rooms:
    def __init__(self , data):
        self.id = data['id']
        self.room_name = data['room_name']
        self.passcode = data['passcode']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] 
 

    @staticmethod
    def validate_room(request):
        is_valid = True
        if len(request['room_name']) < 2:
            flash("please Enter A room name, 'regError'")
            is_valid = False
        elif len(request['room_name']) < 3:
            flash("room Name must be longer than two characters",'regError')
            is_valid = False 
        if len(request['passcode']) < 2:
            flash("please passcode must be longer",'regError')
            is_valid = False
        return is_valid 

    @classmethod
    def insert_room(cls,data):
        query = "INSERT INTO room(room_name,passcode, created_at,updated_at,user_id) VALUES (%(room_name)s,%(passcode)s, NOW(), NOW(), %(users_id)s );"
        return connectToMySQL(mydb).query_db(query,data)


    @classmethod
    def all_room(cls):
        query = "select * from room;"
        results = connectToMySQL(mydb).query_db(query)
            
        all = []
            
        for rams in results:
            all.append( cls(rams) )
        return all


    @classmethod
    def get_one_room(cls,data):
        print(data)
        query = "SELECT * FROM room WHERE room.id =%(id)s;"
        return connectToMySQL(mydb).query_db(query, data)


