import requests

url = "https://api.cheshi.com/services/common/api.php?api=login.Login"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"

}

data = {
    "act": "login",
    "mobile": "13236519712",
    "source": "pc",
    "password": "970722sss",
    "hold_time": "yes"
}

res = requests.post(url, data=data, headers=headers)

admin_url = "https://my.cheshi.com/user/"
admin_res = requests.get(admin_url, headers=headers, cookies=res.cookies)

with open("cheshilogin2.html", "w") as f:
    f.write(admin_res.text)