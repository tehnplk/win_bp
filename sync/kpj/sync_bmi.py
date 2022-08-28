import requests
from datetime import datetime
import time
import mysql.connector
import json

myDb = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='sa',
    password='sa',
    database='log'
)
myDb.autocommit = True
cur = myDb.cursor(dictionary=True)

api_ip = 'http://172.16.30.3'
api_url = f"{api_ip}/api/Visit/UpdateWeightHeight"
api_user = 'kpjwebapi'
api_pass = '4wA0hJ@9Bz'

table = "smart_gate_bmi"


def list_data():
    print(datetime.now(), table, 'begin')
    sql = f"select * from {table} where note1 is null and date(d_update) = CURRENT_DATE"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        time.sleep(1)
        _now = str(datetime.now())
        _now = _now[:-7]
        _id = row['id']
        _json = {
            "HN": row['hn'],
            "Weight": row['bw'],
            "Height": row['bh'],
        }
        print(_now, _json)
        post_data(_id, _json)


def post_data(_id, _data):
    r = requests.post(api_url, json=_data, auth=(api_user, api_pass))
    resp = r.content
    resp = resp.decode('utf-8')
    resp = json.loads(resp)
    print(resp)
    if resp['Status'] == '0':
        sql = f"delete from {table} where id = {_id}"
        cur.execute(sql)
        print('Post Success.')
    else:
        print('Not found vn.')


if __name__ == '__main__':
    while 1:
        list_data()
        time.sleep(15)
