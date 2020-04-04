import os
import mysql.connector

def connect():
    db = mysql.connector.connect(host='remotemysql.com', user='ZEhM9JKxvN', passwd=os.environ['MYSQL_PASSWORD'], database='ZEhM9JKxvN')
    return db


def insert_user(first_name, last_name, email, password, image):
    db = connect()
    cursor = db.cursor()
    sql = 'INSERT INTO user (first_name, last_name, email, password, image)VALUES (%s, %s, %s, %s, %s)'
    val = (first_name, last_name, email, password, image)
    cursor.execute(sql, val)
    db.commit()
    user_id = cursor.lastrowid
    close(db)
    return user_id

def insert_project(title, description, types, image, mem_count):
    db = connect()
    cursor = db.cursor()
    sql = 'INSERT INTO project (title, description, type, image, mem_count) VALUES (%s, %s, %s, %s, %s)'
    val = (title, description, types, image, mem_count)
    cursor.execute(sql, val)
    db.commit()
    project_id = cursor.lastrowid
    close(db)
    return project_id

def insert_friend(sender_id, receiver_id):
    db = connect()
    cursor = db.cursor()
    sql = 'INSERT INTO friend (sender_id, receiver_id) VALUES (%s, %s)'
    val = (sender_id, receiver_id)
    cursor.execute(sql, val)
    db.commit()
    friend_id = cursor.lastrowid
    close(db)
    return friend_id

def insert_likes(user_id, project_id):
    db = connect()
    cursor = db.cursor()
    sql = 'INSERT INTO likes (user_id, project_id) VALUES (%s, %s)'
    val = (user_id, project_id)
    cursor.execute(sql, val)
    db.commit()
    likes_id = cursor.lastrowid
    close(db)
    return likes_id

def insert_comments(user_id, project_id, comment):
    db = connect()
    cursor = db.cursor()
    sql = 'INSERT INTO comments (user_id, project_id, comment)VALUES (%s, %s, %s)'
    val = (user_id, project_id, comment)
    cursor.execute(sql, val)
    db.commit()
    comments_id = cursor.lastrowid
    close(db)
    return comments_id

def insert_project_members(user_id, project_id):
    db = connect()
    cursor = db.cursor()
    sql = 'INSERT INTO project_members (user_id, project_id) VALUES (%s, %s)'
    val = (user_id, project_id)
    cursor.execute(sql, val)
    db.commit()
    project_member_id = cursor.lastrowid
    close(db)
    return project_member_id

def select_project(project_id):
    db = connect()
    cursor = db.cursor()
    sql = 'SELECT title, description, type, image, mem_count FROM project where id = (%s)'
    val = (project_id)
    cursor.execute(sql,val)
    db.commit()
    result = cursor.fetchall()
    close(db)
    return result

def close(db):
    db.close()
