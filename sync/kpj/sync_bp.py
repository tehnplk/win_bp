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
api_url = f"{api_ip}/api/Visit/UpdateOpdVS"
api_user = 'kpjwebapi'
api_pass = '4wA0hJ@9Bz'

table = "smart_gate_bp"


def get_vst_datetime(hn):
    endpoint = f"{api_ip}/api/Patient/GetTodayVisit"
    data = {
        "Keyword": hn
    }
    r = requests.post(endpoint, json=data, auth=(api_user, api_pass))
    resp = r.content
    resp = resp.decode('utf-8')
    resp = json.loads(resp)
    print('RESP Visit', resp)
    if resp['Status'] and resp['Status'] == '0':
        dt = resp['Data']['DocDT']
        # dt = dt.split("T")
        # d = dt[0].strip()
        # t = dt[1][:8].strip()
        # dt = f"{d} {t}"
        return str(dt)
    else:
        return '1980-04-18 11:30:00'


def list_data():
    print(datetime.now(), table, 'begin')
    sql = f"select * from {table} where note1 is null"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        tp = None if row['tp'] == 'None' else row['tp']
        bps = None if row['bps'] == 'None' else row['bps']
        bpd = None if row['bpd'] == 'None' else row['bpd']
        pulse = None if row['pulse'] == 'None' else row['pulse']
        _now = str(datetime.now())[:-7]
        _vst = get_vst_datetime(row['hn'])
        print('Visit date', _vst)
        if _now < _vst:
            _now = _vst
        _id = row['id']
        _json = {
            "HN": row['hn'],
            "RecordDT": _now,
            "Temp": row['tp'],
            "PR": row['pulse'],
            "SystolicBP": row['bps'],
            "DiastolicBP": row['bpd']
        }

        print(_now, _json)
        try:
            post_data(_id, _json)
        except:
            print('Post Error')
            pass


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
