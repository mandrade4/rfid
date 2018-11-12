import uuid
import pandas as pd
import numpy as np
import secrets
import mysql.connector
import string
import random


mydb = mysql.connector.connect(
  host="localhost",
  user="rfid",
  passwd="rfid",
  database="rfid"
)

# print(mydb)

mycursor = mydb.cursor()
uuid=[]
pseudonimo=[]

# sql = "INSERT INTO test (token) VALUES (%s) WHERE id=%s"

# sql = "UPDATE test set token=%s WHERE id=%s"
# val = (str(secrets.token_hex(8)),3)
# mycursor.execute(sql,val)

# Descomentar
# sql = "SELECT uuid FROM test"
# mycursor.execute(sql)
# for row in mycursor.fetchall():
#     uuid.append(row[0])
# print(uuid)

# mydb.commit()



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def find(lista, x):
    i = 0
    for z in lista:
        if z == x:
            return 1,i
        i = i+1
    return -1,i

def createCertificate(y):
    mycursor = mydb.cursor()
    sql = "UPDATE test set pseudonimo=%s WHERE id=%s"
    pseudo = bin(96)
    val = (str(pseudo),y+1)
    mycursor.execute(sql,val)
    mydb.commit()
    print("type",type(pseudo))
    return pseudo

def key_generator():
    # bin=""
    # for j in range(n):
    #     bin+=str(random.randint(0, 1))
    n=random.randint(10,20)
    return bin(n)

def tag(pid2):
    x,y=find(uuid,pid2)
    if x==1:
        return key_generator(),key_generator(),y
    else:
        return 0,0

def reader(id):
        PID2=bin(10)
        k1,k2,position= tag(id)
        if k1+k2==0:
            print("nel")
        # print(k1,k2)    
        # Step 3
        n1 = key_generator()
        n2 = key_generator()

        # Step 4
        A = (int(PID2,2) & int(k1,2) & int(k2,2)) ^ int(n1,2)
        B = (int(PID2,2) & int(k1,2) & int(k2,2)) ^ int(n2,2)
        D = (int(k1,2) & int(n2,2)) ^ (int(k2,2) & int(n1,2))  
        print(A,B,D)

        # Step 5
        E = (int(k1,2) ^ int(n1,2) ^ int(id,2)) ^ (int(k2,2) & int(n2,2))
        F = (int(k1,2) & int(n1,2)) ^ (int(k2,2) & int(n2,2))
        print(E,F) 
        # Actualizando pseudonimos
        PID2 = int(PID2,2) ^ int(n1,2) ^ int(n2,2)
        PID = PID2
        print(PID)

        # # Step 6
        # ID = E ^ (int(k2,2) & int(n2,2)) ^ int(k1,2) ^ int(n1,2)
        # print(id, bin(ID))
        # mycursor = mydb.cursor()
        # sql = "UPDATE test set ptp=%s WHERE id=%s"
        # val = (str(bin(ID)),position+1)
        # mycursor.execute(sql,val)
        # mydb.commit()



def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))
 

if __name__=="__main__":
    # reader('0b1101')
    print("hola")

