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
    @staticmethod
    def validate_post(res):
        is_valid = True
        if len(res['titleofpost']) < 0:
            flash("titleofpost is Required")
            is_valid = False
        elif len(res['titleofpost']) < 3:
            flash("titleofpost must be at least 3 characters.")
            is_valid = False
        if len(res['users_id']) < 0:
            flash(" Date is Required")
            is_valid = False
        return is_valid


    @classmethod 
    def insert_post(cls,data):
        query = "INSERT INTO posts(titleofpost,post, created_at,updated_at,users_id,pokemon_id) VALUES (%(titleofpost)s,%(post)s, NOW(), NOW(), %(users_id)s,%(pokemon_id)s);"
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
 

 
    @classmethod  
    def show_post_by_id(cls,data):
        query = "select * from posts left join pokemon on posts.pokemon_id = pokemon.id left join users on posts.users_id = users.id where posts.id =%(id)s"
        results = connectToMySQL(mydb).query_db(query,data)
        print (results,"this is the results")
        return results
  
    @classmethod  
    def delete_it(cls,data):
        query = "Delete From posts Where id = %(id)s;"
        return connectToMySQL(mydb).query_db(query,data)

    @classmethod
    def edit(cls,data):
        query = "update posts SET titleofpost=%(titleofpost)s, post=%(post)s,pokemon_id=%(pokemon_id)s, updated_at=NOW() WHERE id =  %(id)s;"
        return connectToMySQL(mydb).query_db(query, data) 