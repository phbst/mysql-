from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS
import jwt

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})
app.config['SECRET_KEY'] = 'writting_system_token'

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    cnx = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='2004',
        database='infodb'
    )
    cursor = cnx.cursor()
    query = "SELECT * FROM user WHERE NBXW_USER = %s AND NBXW_PSWD = %s"
    values = (username, password)
    cursor.execute(query, values)
    result = cursor.fetchone()
    cursor.close()
    cnx.close()

    # 检查结果
    if result:
        if username =='renshi':
            id='人事'
        if username =='jishu':
            id='技术'
        if username =='xiaoshou':
            id='销售'
        # 生成JWT token
        token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
        response = {
            'message': 'success',
            'token': token,
            'id':id
        }
    else:
        response = {
            'message': 'error'
        }
    return jsonify(response)
@app.route('/api/write',methods=['POST'])
def write():
    data = request.get_json()
    id= data.get('id')
    title = data.get('title')
    writer = data.get('writer')
    time = data.get('time')
    xwcontent = data.get('xwcontent')
    fla=0

    try:
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='2004',
            database='infodb'
        )

        cursor = cnx.cursor()

        sql = "INSERT INTO xw VALUES (%s, %s, %s, %s, %s,%s)"
        values = (id, title, writer, xwcontent,time,fla)

        # 执行SQL语句
        cursor.execute(sql, values)
        cnx.commit()

        cursor.close()
        cnx.close()
        result="success"

    except Error as e:
        result="error"
    response={
        "code":result
    }
    return jsonify(response)
@app.route('/api/select',methods=['POST'])
def select():
    data = request.get_json()
    type=data.get('type')
    id= data.get('id')
    title = data.get('title')
    writer = data.get('writer')
    time = data.get('time')
    xwcontent = data.get('xwcontent')
    fla=0

    try:
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='2004',
            database='infodb'
        )
        cursor = cnx.cursor()
        sql = "select * from xw"
        cursor.execute(sql)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            if type=="y" and row[5]==1:

                item = {
                    'id': row[0],
                    'title': row[1],
                    'writer': row[2],
                    'time': row[4],
                    'xwcontent': row[3],
                    'fla': row[5]
                }
                result.append(item)
            if type=="w" and row[5]==0:

                item = {
                    'id': row[0],
                    'title': row[1],
                    'writer': row[2],
                    'time': row[4],
                    'xwcontent': row[3],
                    'fla': row[5]
                }
                result.append(item)
            if type=="all":

                item = {
                    'id': row[0],
                    'title': row[1],
                    'writer': row[2],
                    'time': row[4],
                    'xwcontent': row[3],
                    'fla': row[5]
                }
                result.append(item)
        cursor.close()
        cnx.close()


    except Exception as e:
        print('Error executing SELECT query:', str(e))

    return jsonify(result)
@app.route('/api/sys',methods=['POST'])
def sys():
    data = request.get_json()
    try:
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='2004',
            database='infodb'
        )
        cursor = cnx.cursor()
        sql = "select * from employee"
        cursor.execute(sql)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            item = {
                'id': row[0],
                'name': row[1],
                'dpid': row[2],
                'sex':row[3],
                'phone': row[4],
                'email':row[5]
            }
            result.append(item)
        cursor.close()
        cnx.close()


    except Exception as e:
        print('Error executing SELECT query:', str(e))

    return jsonify(result)
@app.route('/api/alter',methods=['POST'])
def alter():
    data = request.get_json()
    type=data.get('type')
    dpid=data.get('dpid')
    xwcontent = data.get('xwcontent')
    fla=0

    try:
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='2004',
            database='infodb'
        )
        cursor = cnx.cursor()
        sql = "select * from xw"
        cursor.execute(sql)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            if type=="y" and row[5]==1 and row[2]==dpid:

                item = {
                    'id': row[0],
                    'title': row[1],
                    'writer': row[2],
                    'time': row[4],
                    'xwcontent': row[3],
                    'fla': row[5]
                }
                result.append(item)
            if type=="w" and row[5]==0 and row[2]==dpid:

                item = {
                    'id': row[0],
                    'title': row[1],
                    'writer': row[2],
                    'time': row[4],
                    'xwcontent': row[3],
                    'fla': row[5]
                }
                result.append(item)
            if type=="all" and row[2]==dpid:

                item = {
                    'id': row[0],
                    'title': row[1],
                    'writer': row[2],
                    'time': row[4],
                    'xwcontent': row[3],
                    'fla': row[5]
                }
                result.append(item)
        cursor.close()
        cnx.close()


    except Exception as e:
        print('Error executing SELECT query:', str(e))

    return jsonify(result)
@app.route('/api/save',methods=['POST'])
def save():
    data = request.get_json()
    new_content = data.get('newcontent')
    xw_id = data.get('xwid')

    try:
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='2004',
            database='infodb'
        )
        cursor = cnx.cursor()

        # 更新语句，这里假设你有一个名为 'xw' 的表，且该表有 'XW_ID' 和 'XW_CONTEXT' 列
        update_sql = "UPDATE xw SET XW_CONTEXT = %s WHERE XW_ID = %s"
        cursor.execute(update_sql, (new_content, xw_id))
        cnx.commit()

        cursor.close()
        cnx.close()

        return jsonify({'code': '200'})
    except Exception as e:
        return jsonify({'code': '401', 'error': str(e)})

    return jsonify(result)
@app.route('/api/sent',methods=['POST'])
def sent():
    data = request.get_json()
    dp_id = data.get('dpid')
    xw_id = data.get('xwid')

    try:
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='2004',
            database='infodb'
        )
        cursor = cnx.cursor()

        sent1_sql = "SELECT * FROM xw WHERE XW_ID =%s"
        cursor.execute(sent1_sql, (xw_id,))
        row = cursor.fetchall()[0]


        sent2_sql = "INSERT INTO xwcl VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sent2_sql, (row[0], row[1], row[2], dp_id, row[3], row[4], "无"))
        #
        update_sql = "UPDATE xw SET XW_FLAG = %s WHERE XW_ID = %s"
        cursor.execute(update_sql, ("1", xw_id))

        cnx.commit()

        cursor.close()
        cnx.close()

        return jsonify({'code': '200'})
    except Exception as e:
        return jsonify({'code': '401', 'error': str(e)})
@app.route('/api/recive',methods=['POST'])
def recive():
    data = request.get_json()
    id= data.get('id')
    try:
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='2004',
            database='infodb'
        )
        cursor = cnx.cursor()
        sql = "select * from xwcl where XW_RECEIVER=%s"
        cursor.execute(sql,(id,))
        rows = cursor.fetchall()
        result = []
        for row in rows:
            item = {
                'id': row[0],
                'title': row[1],
                'writer': row[2],
                'reciver':row[3],
                'xwcontent': row[4],
                'time': row[5],
                'dcp': row[6]
            }
            result.append(item)
        cursor.close()
        cnx.close()


    except Exception as e:
        print('Error executing SELECT query:', str(e))

    return jsonify(result)
@app.route('/api/edit',methods=['POST'])
def edit():
    data = request.get_json()
    id= data.get('id')
    content=data.get('content')
    try:
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='2004',
            database='infodb'
        )
        cursor = cnx.cursor()
        sql = "update  xwcl set XW_REMARK=%s where XW_ID=%s"
        cursor.execute(sql,(content,id))
        cnx.commit()

        cursor.close()
        cnx.close()

        return jsonify({'code': '200'})
    except Exception as e:
        return jsonify({'code': '401', 'error': str(e)})

if __name__ == '__main__':
    app.run(port=3000,debug=True)
