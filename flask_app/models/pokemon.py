from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mydb = 'poke_social_media'
class Pokemons:
    def __init__( self , data ): 
        self.id = data['id']
        self.content = data['name']
        self.content = data['type']
        self.content = data['species']
        self.content = data['height']
        self.content = data['weight']
        self.content = data['abilites']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
 
    @classmethod
    def show_all_pokemon(cls):
        query = "select * from pokemon"
        results = connectToMySQL(mydb).query_db(query)
        print (results)
        return results
    @classmethod
    def showjoin(cls,data):
        query = "select * from pokemon left join posts on posts.pokemon_id = pokemon.id left join users on posts.users_id = users.id where posts.id =%(id)s"
        results = connectToMySQL(mydb).query_db(query,data)
        print (results)
        return results