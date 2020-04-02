import os
import mysql.connector

def connect():
    server = 'remotemysql.com:3306'
    user = 'ZEhM9JKxvN'
    passwd = os.environ['MYSQL_PASSWORD']
    database = 'ZEhM9JKxvN'
    db = mysql.connector.connect(server, user, passwd, database)
    return db


def insert_user(first, last, email, passwd, image):
    db = connect()
    cursor = db.mycursor()
    sql = 'INSERT INTO user VALUES (%s, %s, %s, %s, %s)'
    val = (first, last, email, passwd, image)
    cursor.execute(sql, val)
    db.commit()
    user_id = cursor.lastrowid
    close(db)
    return user_id

def insert_project(title, description, skills, types, image):
    db = connect()
    cursor = db.mycursor()
    sql = 'INSERT INTO project VALUES (%s, %s, %s, %s, %s)'
    val = (title, description, skills, types, image)
    cursor.execute(sql, val)
    db.commit()
    project_id = cursor.lastrowid
    close(db)
    return project_id

def insert_friend(sender_id, receiver_id):
    db = connect()
    cursor = db.mycursor()
    sql = 'INSERT INTO friend VALUES (%s, %s)'
    val = (sender_id, receiver_id)
    cursor.execute(sql, val)
    db.commit()
    friend_id = cursor.lastrowid
    close(db)
    return friend_id

def insert_likes(user_id, project_id):
    db = connect()
    cursor = db.mycursor()
    sql = 'INSERT INTO likes VALUES (%s, %s)'
    val = (user_id, project_id)
    cursor.execute(sql, val)
    db.commit()
    likes_id = cursor.lastrowid
    close(db)
    return likes_id

def insert_comments(user_id, project_id, comment):
    db = connect()
    cursor = db.mycursor()
    sql = 'INSERT INTO comments VALUES (%s, %s, %s)'
    val = (user_id, project_id, comment)
    cursor.execute(sql, val)
    db.commit()
    comments_id = cursor.lastrowid
    close(db)
    return comments_id

def insert_project_members(user_id, project_id):
    db = connect()
    cursor = db.mycursor()
    sql = 'INSERT INTO project_members VALUES (%s, %s)'
    val = (user_id, project_id)
    cursor.execute(sql, val)
    db.commit()
    project_member_id = cursor.lastrowid
    close(db)
    return project_member_id

def close(db):
    db.close()
