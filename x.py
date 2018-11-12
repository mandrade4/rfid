import mysql.connector
from dbfread import DBF


for record in DBF('xd.dbf'):
    print(record)