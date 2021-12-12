import psycopg2


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


#saves changes on database
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


def getleveltable():
    query = """select * from public."Words where " """


def savename(object):
    query = f"""insert into public."Users" (user_name,password,total_time,current_level) values ('{object.name}','{object.password}','{object.totaltime}','{object.level}')"""
    cur.execute(query)
    conn.commit()


def bringallnames():
    query = """select * from public."Users" """
    info = cur.execute(query)
    info = cur.fetchall()
    return info
