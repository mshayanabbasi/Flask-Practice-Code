# models.py
from sqlalchemy import Table, Column, Integer, Text
from sqlalchemy.orm import mapper
from database import metadata, db_session
import re

class BlogPost(object):
    query = db_session.query_property()
    def __init__(self, FU_ID, FU_TYPE, FU_FIRSTNAME, FU_LASTNAME, FU_EMAIL, FU_COM_EMAIL, fb_likes):
        self.id = re.sub(r'.*-TRIAL-', '', FU_ID)[:FU_ID.rindex(' ')]
        self.type = re.sub(r'.*-TRIAL-', '', FU_TYPE)[:FU_TYPE.rindex(' ')]
        self.fname = re.sub(r'.*-TRIAL-', '', FU_FIRSTNAME)[:FU_FIRSTNAME.rindex(' ')]
        self.lname = re.sub(r'.*-TRIAL-', '', FU_LASTNAME)[:FU_LASTNAME.rindex(' ')]
        self.email = re.sub(r'.*-TRIAL-', '', FU_EMAIL)[:FU_EMAIL.rindex(' ')]
        self.COM_EMAIL = re.sub(r'.*-TRIAL-', '', FU_COM_EMAIL)[:FU_COM_EMAIL.rindex(' ')]
        self.fb_likes = re.sub(r'.*-TRIAL-', '', fb_likes)[:fb_likes.rindex(' ')]

blog_posts = Table('user_cards', metadata,
    Column('FU_ID', Integer, primary_key=True),
    Column('FU_TYPE', Text),
    Column('FU_FIRSTNAME', Text),
    Column('FU_LASTNAME', Text),
    Column('FU_EMAIL', Text),
    Column('FU_COM_EMAIL', Text),
    Column('FU_PHONE', Text),
    Column('FU_GENDER', Text),
    Column('FU_DISPLAYNAME', Text),
    Column('FU_IMG', Text),
    Column('FU_COUNTRY_CODE', Text),
    Column('address', Text),
    Column('address2', Text),
    Column('fb_likes', Integer),
    Column('fb_friends', Integer),
    Column('twitter_followers', Integer),
    Column('google_followers', Integer),
    Column('blog_monthly_views', Integer),
    Column('vine_followers', Integer),
    Column('youtube_subs', Integer),
    Column('facebook_id', Text),
    Column('twitter_id', Text),
    Column('google_id', Text),
    Column('instagram_id', Text),
    Column('vine_id', Text),
    Column('youtube_id', Text),
    Column('ip_amount', Text),
    Column('facebook_id', Text)
)

mapper(BlogPost, blog_posts)