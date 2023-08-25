import requests

def http_get(url,params):
    header = {"Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVSUQiOjI3MTAsIk1vYmlsZSI6IjE3NzcyOTQ5MDM5IiwiTmFtZSI6ImNoZW5oZW5nIiwiRGV2aWNlIjoiY2RuLW1hbmFnZXIiLCJleHAiOjQ4NDY1Mjk2NDIsImlzcyI6ImFkbWluIn0.isdf7gbxluDyZJaUacGRlXewPO_AHPH6T1jPw9qhQaM"}
    res = requests.get(url,headers=header,params=params)
    print("res is ",res.content)
    return res

def http_post(url,body):
    header = {}
    res = requests.post(url,data=body)
    return res

if __name__ == '__main__':
    url = "http://domain:8000/host"
    dict = {"curPage":1,"pageSize":10}
    http_get(url,dict)
    http_post(url)
