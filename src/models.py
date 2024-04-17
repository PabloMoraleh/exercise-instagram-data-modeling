import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    comment = relationship('Comment', backref='user', lazy=True)
    followers = relationship('Follower', backref='user', lazy=True)
    posts = relationship('Post', backref= 'user', lazy=True)

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    post_text = Column(String(255), nullable=False)
    media = relationship('Media', backref='posts', lazy=True)

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    type = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False)

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    comment_text = Column(String(255), nullable=False)

class Follower(Base):
    __tablename__ = 'followers'

    user_from_id = Column(Integer, ForeignKey('user.id'),primary_key=True, nullable= False)
    user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True, nullable = False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
