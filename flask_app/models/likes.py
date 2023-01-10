from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mydb = 'poke_social_media'
class Like:
    def __init__( self , data ):
        self.id = data['id']
        self.content = data['numlikes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod 
    def insert_messages(cls,data):
        query = "INSERT INTO likes(numlikes, created_at,updated_at,post_id,user_id) VALUES (%(numlikes)s, NOW(), NOW(), %(post_id)s,  %(users_id)s  );"
        return connectToMySQL(mydb).query_db(query,data)