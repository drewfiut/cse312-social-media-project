import os
import mysql.connector

#CONNECT FUNCTION
def connect():
    db = mysql.connector.connect(host='remotemysql.com', user='ZEhM9JKxvN', passwd=os.environ['MYSQL_PASSWORD'], database='ZEhM9JKxvN')
    return db

#INSERT FUNCTIONS

#Inserts a new user into the user table
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

#Inserts a new project into the project table
def insert_project(title, description, types, image, mem_count, auth_id):
    db = connect()
    cursor = db.cursor()
    sql = 'INSERT INTO project (title, description, type, image, mem_count, auth_id) VALUES (%s, %s, %s, %s, %s, %s)'
    val = (title, description, types, image, mem_count, auth_id)
    cursor.execute(sql, val)
    db.commit()
    project_id = cursor.lastrowid
    close(db)
    return project_id

#Inserts a friends relationship into the friend table
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

#Inserts a like into the likes table
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

#inserts a comment into the comments table
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

#Inserts a project member relationship into the project_members table
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

#SELECT FUNCTIONS

#Selects a user from the user table
def select_user(user_id):
    db = connect()
    cursor = db.cursor()
    sql = 'SELECT first_name, last_name, email, password, image FROM user WHERE id = (%s)'
    val = (user_id,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    close(db)
    return result

#Selects a user from the user table by email
def select_user_email(email):
    db = connect()
    cursor = db.cursor()
    sql = 'SELECT id, first_name, last_name, password, image FROM user WHERE email = (%s)'
    val = (email,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    close(db)
    return result

#Selects a project from the project table
def select_project(project_id):
    db = connect()
    cursor = db.cursor()
    sql = 'SELECT title, description, type, image, mem_count, auth_id FROM project WHERE id = (%s)'
    val = (project_id,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    close(db)
    return result

#Selects all project from the project table
def select_projects_all():
    db = connect()
    cursor = db.cursor()
    sql = 'SELECT title, description, type, image, mem_count, id FROM project'
    val = ()
    cursor.execute(sql,val)
    result = cursor.fetchall()
    close(db)
    return result

#Selects all friend relationships of given user from friends table
def select_friends(user_id):
    db = connect()
    cursor = db.cursor()
    sql = 'SELECT sender_id, receiver_id FROM friend WHERE sender_id = (%s) OR receiver_id = (%s)'
    val = (user_id, user_id)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    close(db)
    return result

#Selects all comments on a project
def select_comment_project(project_id):
    db = connect()
    cursor = db.cursor()
    sql = 'SELECT user_id, comment FROM comments WHERE project_id = (%s)'
    val = (project_id,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    close(db)
    return result

#Selects all comments left by a user
def select_comment_user(user_id):
    db = connect()
    cursor = db.cursor()
    sql = 'SELECT project_id, comment FROM comments WHERE user_id = (%s)'
    val = (user_id,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    close(db)
    return result

#Selects number of likes on a project
def select_likes_count(project_id):
    db = connect()
    cursor = db.cursor()
    sql = 'SELECT COUNT(*) FROM likes WHERE project_id = (%s)'
    val = (project_id,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    close(db)
    return result

#checks if a user liked a post
def is_liked(user_id, project_id):
    db = connect()
    cursor = db.cursor()
    sql = 'SELECT COUNT(*) FROM likes WHERE user_id = (%s) and project_id = (%s)'
    val = (user_id, project_id)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    close(db)
    if result[0][0] == 0:
        return False
    else:
        return True

#Selects all projects a user has liked
def select_likes_user(user_id):
    db = connect()
    cursor = db.cursor()
    sql = 'SELECT project_id FROM likes WHERE user_id = (%s)'
    val = (user_id,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    close(db)
    return result

#Selects all members of a project
def select_project_members(project_id):
    db = connect()
    cursor = db.cursor()
    sql = 'SELECT user_id FROM project_members WHERE project_id = (%s)'
    val = (project_id,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    close(db)
    return result

#Selects all projects a user is a  member of
def select_member_projects(user_id):
    db = connect()
    cursor = db.cursor()
    sql = 'SELECT project_id FROM project_members WHERE user_id = (%s)'
    val = (user_id,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    close(db)
    return result

#CLOSE FUNCTION
def close(db):
    db.close()
