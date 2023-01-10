from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mydb = 'poke_social_media'
 
class posts:
    def __init__( self , data ):
        self.id = data['id'] 
        self.titleofpost = data['titleofpost']
        self.post = data['post']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] 


  
    @classmethod 
    def insert_post(cls,data):
        query = "INSERT INTO posts(titleofpost,post, created_at,updated_at,users_id) VALUES (%(titleofpost)s,%(post)s, NOW(), NOW(), %(users_id)s);"
        results = connectToMySQL(mydb).query_db(query,data)
        print(results)
        return results
    @classmethod
    def show_posts(cls):
        query =  "select * from posts left join users on users_id = users.id" 
        return connectToMySQL(mydb).query_db(query)


    @classmethod
    def showmypost(cls,data):
        query = "select * from posts where users_id = %(id)s"
        results = connectToMySQL(mydb).query_db(query,data)
        print (results)
        return results