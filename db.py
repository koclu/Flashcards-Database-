import psycopg2
from PyQt5 import QtCore

"""

# create a cursor
cur = conn.cursor()

# execute a statement
cur.execute("
    SELECT * from public."Artist";
    ")

# display the result of executed SQL query
info = cur.fetchall() # you can also use fetchone() and fetchmany() according to your need
print(info)

# close the communication with the PostgreSQL
cur.close()


# saves changes on database
conn.commit()


"""

conn = psycopg2.connect(
    host="localhost",
    database="Flashcard",
    user='postgres',
    password=1)
try:

    cur = conn.cursor()
except (Exception) as error:
    print(error)

sql_query = """

select * from public."Words"

"""


def savedatabase(query):
    """
    function takes 1 arguement which is saving database.
    """
    cur.execute(query)
    conn.commit()


def checkname(name):
    query = f"""select * from public."Users" where user_name = '{name}' """
    cur.execute(query)
    info = cur.fetchall()
    if len(info) == 1:
        return True
    else:
        return False


def getleveltable(user_object):
    query = f"""select w.words_id, w.dutch,w.english
    from public."Words" as w
    join public."Users" as u
    on u.current_level = w.words_of_level
    where u.user_name = '{user_object.name}'
    """
    info = cur.execute(query)
    info = cur.fetchall()
    return info


def gettemporarylevel(user_object):
    query = f"""select w.words_id, w.dutch,w.english
    from public."Words" as w
    join public."Users" as u
    on {user_object.temporary_level} = w.words_of_level
    where u.user_name = '{user_object.name}'
    """
    info = cur.execute(query)
    info = cur.fetchall()
    return info


def getcustomlevels(user_object):
    query = f"""select dutch,english
    from public."Custom_levels" as c
    join public."Users" as u
    on u.user_name = c.user_name
    where u.user_name = '{user_object.name}' and c.level_name = '{user_object.customlevelname}'
    """
    cur.execute(query)
    info = cur.fetchall()
    return info


def savename(user_object):
    query = f"""insert into public."Users" (user_name,password,total_time,current_level) values ('{user_object.name}','{user_object.password}',{user_object.totaltime},{user_object.level})"""
    cur.execute(query)
    conn.commit()


def bringallnames():
    query = """select * from public."Users" """
    info = cur.execute(query)
    info = cur.fetchall()
    return info


def updatelevel(user_object):
    query = f""" update public."Users" Set current_level = {user_object.level} where user_name = '{user_object.name}' """
    cur.execute(query)
    conn.commit()


def save_user(user_object):
    query = f"""update public."Users" Set user_name = '{user_object.name}' ,
                                    total_time = {user_object.totaltime} ,
                                    current_level = {user_object.level}
                                    where user_name = '{user_object.name}'"""
    cur.execute(query)
    conn.commit()


def calculate_totalprogress(user_object):
    # return (self.level * 100) / (len(self.wordsid)/20)
    query = f"""select current_level from public."Users" where user_name = '{user_object.name}' """
    query2 = f"""select count(words_id) from public."Words" """
    info = (cur.execute(query))
    info = cur.fetchall()
    level = info[0][0]
    info2 = (cur.execute(query2))
    info2 = cur.fetchall()
    total_of_words = info2[0][0]
    return ((level * 100) / (total_of_words/20))


def add_level(user_object, list, levelname):

    for word in list:
        if len(word[0]) == 0 or len(word[1]) == 0:
            continue
        cur.execute(
            f""" insert into public."Custom_levels"(user_name,level_name,dutch,english)
        VALUES ('{user_object.name}','{levelname}','{word[0]}','{word[1]}')""")
        conn.commit()


def getcustomlevelname(user_object):
    query = f"""select distinct c.level_name
    from public."Custom_levels" as c
    join public."Users" as u
    on u.user_name = c.user_name
    where u.user_name = '{user_object.name}'
    """
    cur.execute(query)
    info = cur.fetchall()
    return info


def updatestatistics(user_object):
    query = f""" insert into public."Statistics"(user_name, completed_level, attemps, knows)
        VALUES('{user_object.name}', {user_object.level}, {user_object.Attempts}, {user_object.atOnce}) on conflict(user_name, completed_level)
        do update set attemps = {user_object.Attempts}, knows = {user_object.atOnce}"""
    cur.execute(query)
    conn.commit()
    user_object.Attempts = 0
    user_object.atOnce = 0


def updatestatistics_temporary(user_object):
    query = f""" insert into public."Statistics"(user_name, completed_level, attemps, knows)
        VALUES('{user_object.name}', {user_object.temporary_level}, {user_object.Attempts}, {user_object.atOnce}) on conflict(user_name, completed_level)
        do update set attemps = {user_object.Attempts}, knows = {user_object.atOnce}"""
    cur.execute(query)
    conn.commit()
    user_object.Attempts = 0
    user_object.atOnce = 0
