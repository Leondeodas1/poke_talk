from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mydb = 'poke_social_media'
  
class something:
    def __init__( self , data ):
        self.id = data['id']
        self.news = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']   


    @classmethod
    def savenews(cls, data ):
        print(data)
        return data