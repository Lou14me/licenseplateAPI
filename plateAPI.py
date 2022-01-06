from flask import Flask
import pymysql
from flask import request
import json

app = Flask(__name__)

@app.route('/add', methods=['get', 'post'])
def add():
    if request.method == 'GET':
        plate1 = request.values.get('plate')
        label1 = request.values.get('label')

    elif request.method == 'POST':
        try:
            plate1 = request.form['plate']
            label1 = request.form['label']
        except KeyError:
            ret = {'code': 10001, 'message': 'VALUES NOT NULL'}
            return json.dumps(ret, ensure_ascii=False)

    if  plate1 and label1:
        db = pymysql.connect(host="localhost",port = 3306, user="root", password="password", database="sql_tutorial")
        cursor = db.cursor()
        sql = "insert into car(plate,label) values ('"+ plate1 +"'," +label1+ ")"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            return 'SUCCESS'
        except Exception as e:
            db.rollback()
            return 'FAIL'
        finally:
            db.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
