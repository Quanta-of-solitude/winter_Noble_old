import os
import psycopg2


DATABASE_URL = os.environ.get("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

def create_Tables():

    command = ("""CREATE TABLE welcomeyou (serverid VARCHAR,welcomemsg VARCHAR,channelid VARCHAR,welcometype VARCHAR,welcomeswitch VARCHAR, welcomelinkimage VARCHAR)""")
    cur.execute(command)
    command2 = ("""CREATE TABLE leaveyou (serverid VARCHAR,channelid VARCHAR,leavemsg VARCHAR,leavewitch VARCHAR)""")
    cur.execute(command2)
    command3 = ("""CREATE TABLE autoroler (serverid VARCHAR,roleidname VARCHAR,roleswitch VARCHAR)""")
    cur.execute(command3)

cur.close()
conn.close()
