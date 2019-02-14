# app.py
from flask import Flask, render_template, json, request, jsonify
from flask_restplus import Resource, Api, fields
from database import db_session
from models import BlogPost
from flask_caching import Cache

application = Flask(__name__)
api = Api(application,
          version='0.1',
          title='DEV API',
          description='FU_USER TEST API',
)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route('/fu_user')
class BlogPosts(Resource):
    model = api.model('Model', {
        'FU_ID': fields.Integer,
        'FU_TYPE': fields.String,
        'FU_FIRSTNAME': fields.String,
        'FU_LASTNAME': fields.String,
        'FU_EMAIL': fields.String,
        'FU_COM_EMAIL': fields.String,
        'FU_PHONE': fields.String,
        'FU_GENDER': fields.String,
        'FU_DISPLAYNAME': fields.String,
        'FU_IMG': fields.String,
        'FU_COUNTRY_CODE': fields.String,
        'address': fields.String,
        'address2': fields.String,
        'fb_likes': fields.Integer,
        'fb_friends': fields.Integer,
        'twitter_followers': fields.Integer,
        'google_followers': fields.Integer,
        'blog_monthly_views': fields.Integer,
        'vine_followers': fields.Integer,
        'youtube_subs': fields.Integer,
        'facebook_id': fields.String,
        'twitter_id': fields.String,
        'google_id': fields.String,
        'instagram_id': fields.String,
        'vine_id': fields.String,
        'youtube_id': fields.String,
        'ip_amount': fields.String,
        'facebook_id': fields.String
    })


        

    
         
    @api.marshal_with(model, envelope='resource')
    def get(self, **kwargs):
        return BlogPost.query.all()
@application.route('/fu_user_data', methods=['POST'])
def find():
    FU_ID = request.get_json(silent=True)
    if FU_ID is None:
        return "Sorry You cant get data Please Try again"
    value = FU_ID.get('id', None)
    if value == None:
        return "Sorry You cant get data Please Try again"
    userId = (FU_ID['id'])
    data = BlogPost.query.filter_by(FU_ID=userId).first()
    print(data)
    if not data:
        return jsonify({'message':'We cannot find the id'})
    else:
        in_data = {
        'FU_ID': data.FU_ID,
        'FU_TYPE' : data.FU_TYPE,
        'FU_FIRSTNAME' : data.FU_FIRSTNAME,
        'FU_LASTNAME' : data.FU_LASTNAME,
        'FU_EMAIL' : data.FU_EMAIL,
        'FU_COM_EMAIL' : data.FU_COM_EMAIL,
        'FU_PHONE' : data.FU_PHONE,
        'FU_GENDER' : data.FU_GENDER,
        'FU_DISPLAYNAME' : data.FU_DISPLAYNAME,
        'FU_IMG'  : data.FU_IMG,
        'FU_COUNTRY_CODE' : data.FU_COUNTRY_CODE,
        'address' : data.address,
        'address2' : data.address2,
        'fb_likes' : data.fb_likes,
        'fb_friends' : data.fb_friends,
        'twitter_followers' : data.twitter_followers,
        'google_followers' : data.google_followers,
        'blog_monthly_views' : data.blog_monthly_views,
        'vine_followers' : data.vine_followers,
        'youtube_subs' : data.youtube_subs,
        'facebook_id' : data.facebook_id,
        'twitter_id': data.twitter_id,
        'google_id' : data.google_id,
        'instagram_id' : data.instagram_id,
        'vine_id' : data.vine_id,
        'youtube_id' : data.youtube_id,
        'ip_amount' : data.ip_amount,
        'facebook_id': data.facebook_id
        }
        return jsonify(in_data)
@application.route("/loaderio-677465338011948391207ba45f29be67/")
def index():
   return render_template("loaderio-677465338011948391207ba45f29be67.txt")

@application.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=8080)