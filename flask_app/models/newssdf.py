from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mydb = 'poke_social_media'
  


class newson:
    def __init__( self , data ):
        self.id = data['id']
        self.news = data['news']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] 
 
    @classmethod 
    def save_news(cls,data):
        query = "INSERT INTO news(news,created_at,updated_at,users_id) VALUES (%(news)s, NOW(), NOW(), %(users_id)s);"
        results = connectToMySQL(mydb).query_db(query,data)
        print(results)
        return results
    
    @classmethod
    def getnews(cls,data):
        query =  "select * from news left join users on users_id = %(id)s ORDER BY news.id desc" 
        results = connectToMySQL(mydb).query_db(query,data)
        for info in results:
            print(info)
        try:
            from googlesearch import search
        except ImportError:

        #     print("No module named 'google' found")
        # query = data
    
        # for news in search(query, tld="co.in", num=10, stop=10, pause=2):
        #     print ("hello",news
            return query