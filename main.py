import json
import requests
import os.path

config = None
with open('config.json', 'r') as f:
    config = json.load(f)

dataStart = {
    "page":"messanger",
    "staticKey":"kaka",
    "deviceID":None,
    "account":{
        "active": False,
        "password": None,
        "name":None,
        "tag":None,
        "email":None,
        "number":None,
        "id":None,
        "conf":{
            "blackList":{},
            "ViewNumber":True,
            "ViewTime":True,
            "ViewEmail":False,
            "ViewIcon":True,
            "resandMessage":True,
            "collin":True,
            "gs":True,
            "sendMessage":True,
            "ViewdateOfBirthday":True,
            "ViewSubtitle":True
        }
    }
}
userData:json
if not os.path.exists('./data.json'):
    with open('data.json', 'w') as f:
        json.dump(dataStart, f)
with open('data.json', 'r') as f:
    userData = json.load(f)
def save_data():
    with open('data.json', 'w') as f:
        json.dump(userData, f)
while True:
    message = input(">> ").lower()
    if message == "stop":
        exit()
    elif message == "1":
        header = {"my_id": userData["account"]["id"], "deviceID":str(userData["deviceID"])}
        print(header)
        r = requests.get(f"http://{config['SERVER_IP']}:{config['SERVER_PORT']}", headers=header)
        print(r.json())
    else:
        login = "kretoff"
        password = "1234"
        m = message.split(" ")
        if m[0] == "sandreg":
            data = {"email":m[1]}
            dataJ = json.dumps(data)
            r = requests.post(f"http://{config['SERVER_IP']}:{config['SERVER_PORT']}/sandReg", data=dataJ)
            print(r.json())
        elif m[0] == "test":
            i = 0
            for i in range(0, int(m[1])):
                r = requests.get(f"http://{config['SERVER_IP']}:{config['SERVER_PORT']}/test")
                print(r.json())
                i+=1
        elif m[0] =="reg":
            data = {"cod":m[1], "tag":m[2], "password":m[3], "email":m[4], "id":m[5]}
            dataJ = json.dumps(data)
            r = requests.post(f"http://{config['SERVER_IP']}:{config['SERVER_PORT']}/reg", data=dataJ)
            data = r.json()
            if data['data'] == 'goodRegistration':
                userData['staticKey'] = data['key']
                userData["account"]["active"] = True
                userData["account"]["tag"] = data["tag"]
                userData["account"]["email"] = data["email"]
                userData["account"]["id"] = data["id"]
                save_data()
        elif m[0] == "login":
            data = {"tag":m[1], "password":m[2]}
            dataJ = json.dumps(data)
            r = requests.post(f"http://{config['SERVER_IP']}:{config['SERVER_PORT']}/login", data=dataJ)
            data = r.json()
            if data["data"] =="goodLogin":
                print("good login")
                userData["staticKey"] = data["key"]
                userData["deviceID"] = data["deviceID"]
                userData["account"]["active"] = True
                userData["account"]["name"] = data["userInfo"]["login"]
                userData["account"]["tag"] = data["userInfo"]["tag"]
                userData["account"]["email"] = data["userInfo"]["email"]
                userData["account"]["number"] = data["userInfo"]["num"]
                userData["account"]["id"] = data["userInfo"]["userID"]
                save_data()
            else:print("no logined")
        else:print("Sorry, but I don't understand you")