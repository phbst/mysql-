from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS
import jwt

def sent():

    dp_id = 3
    xw_id = 2

    try:
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='2004',
            database='infodb'
        )
        cursor = cnx.cursor()

        sent1_sql = "SELECT * FROM xw WHERE XW_ID = %s"
        cursor.execute(sent1_sql, (xw_id,))
        row = cursor.fetchall()[0]
        print(row)
        sent2_sql = "INSERT INTO xwcl VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sent2_sql, (row[0], row[1], row[2], dp_id, row[3], row[4], "无"))

        cnx.commit()

        cursor.close()
        cnx.close()

        print('ok')
    except Exception as e:
        print(str(e))
if __name__ == '__main__':
    sent()
