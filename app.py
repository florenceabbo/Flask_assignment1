from flask import Flask, jsonify

# Creating an instance app
app =Flask (__name__)
@app.route("/")  #They are denoted by by @ followed by the instance and denoted by a /.
def hello_world():
    return "<p>These are my articles</>"

@app.route("/articles", methods=['GET']) 
def get_articles():
          articles = {
            "Article1":{
                "id":1,
                "title":"Elementary codding",
                "body":"Teaching computer programming to youth can prepare them for the future job market, promote equity in tech professions and develop students’ computational thinking skills",
                "author":"Abbo Fulumera"
            },
            "Article2":{
                "id":2,
                "title":"Hackathons should be renamed to avoid negative connotations",
                "body":"When you break out the game console to play a video game like NBA2K, chances are the biggest decision you’ll have to make is which player or team you want to be. But have you ever considered becoming one of the people who actually designs a game like NBA2K",
                "author":"P. Alison Paprica"

            },
             "Article3":{
                "id":3,
                "title":"5 ways to break into the video game industrys",
                "body":"“Hackathons” can imply breaching security and privacy. To more accurately reflect their creative and constructive intent, they can be referred to instead as “datathons” or “code fests.”",
                "author":"André Thomas"
            }
          }
          return jsonify(articles)


if __name__=='main':
    app.run(debug=True)
     
       
    