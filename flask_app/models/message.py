from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mydb = 'poke_social_media'
  
class messages:
    def __init__( self , data ):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] 
 
    @staticmethod
    def validate_message(request):
        is_valid = True
        if len(request['content']) < 2:
            flash("please Enter A message")
            is_valid = False
        elif len(request['content']) < 3:
            flash("message must be longer",)
            is_valid = False 
        return is_valid 

 

    @classmethod 
    def insert_messages(cls,data):
        query = "INSERT INTO messages(content, created_at,updated_at,room_id,user_id) VALUES (%(content)s, NOW(), NOW(), %(room_id)s,  %(users_id)s  );"
        return connectToMySQL(mydb).query_db(query,data)

    @classmethod
    def show_all_messages(cls,data):
        query =  "SELECT * FROM room LEFT JOIN messages on messages.room_id = room.id LEFT Join users on messages.user_id = users.id where room.id = %(id)s;"
        return connectToMySQL(mydb).query_db(query,data)


    # @classmethod
    # def show_all_(cls,data):
    #     query = "SELECT * FROM room LEFT JOIN users on users.id where room.id = %(id)s;"
    #     return connectToMySQL(mydb).query_db(query,data)

            # query = "SELECT * FROM room LEFT JOIN users on users.id where room.id = %(id)s;"
            # "SELECT * FROM messages where room_id = %(id)s