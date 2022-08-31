import requests
import time
import schedule

api_host = 'http://localhost:3000'
end_point_get_visit = "patient/get_today_visit_by_cid"
end_point_post_data = "bp/post_data_bp"


def get_today_visit(cid):
    r = requests.get(f"{api_host}/{end_point_get_visit}/{cid}")
    resp = r.json()
    if resp:
        return resp['visit_number'], resp['visit_date'], resp['visit_time']
    else:
        return None, None, None


def sync():
    r = requests.get(f"{api_host}/patient/test")
    print(r.content.decode())


if __name__ == '__main__':
    schedule.every(5).seconds.do(sync)

    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)
