import requests

url = "https://my.cheshi.com/user/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

cookies = "pv_uid=1692344482758; pv_source=; cheshi_UUID=01H83SEY1YZY41FDGMSFQN8EFY; Hm_lvt_8fe47348e12ba11be217fd389b115472=1692344493; lv=1692943890; vn=5; cheshi_pro_city=Ml/kuIrmtbdfMThf6buE5rWm5Yy6X3NoYW5naGFp; Hm_lvt_ed9cf33799965fb6c868762ac84e663e=1692943900; Hm_lpvt_ed9cf33799965fb6c868762ac84e663e=1692944380; cheshi_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6ImNoZXNoaV9oNV9zaWduIn0.eyJpc3MiOiJodHRwczpcL1wvYXBpLmNoZXNoaS5jb20iLCJhdWQiOiJodHRwczpcL1wvYXBpLmNoZXNoaS5jb20iLCJqdGkiOiJjaGVzaGlfaDVfc2lnbiIsImlhdCI6MTY5Mjk0NDQ5NywibmJmIjoxNjkyOTQ0NTU3LCJleHAiOjE2OTM1NDkyOTcsInVpZCI6IjkwNzkzNzQifQ.TDCYKOL8kiE5Fbc0_ip6QKCEc-M31MTPeLi3WDXdyd0; cheshi_user_authv2=MzIyODE2MwlKYXZhRWRnZQl2MgliY2Q2MzFkODQ2ZTE0OGVkMGNlM2U4YTExZGExNmJkMQkxNjkyOTQ0NDk3CWI3OGMwOGVjODM1YzE5MjAzYmM2ODlhMGMxZDIxMzAy; cheshi_user_info=OTA3OTM3NAlKYXZhRWRnZQl2MgliY2Q2MzFkODQ2ZTE0OGVkMGNlM2U4YTExZGExNmJkMQkxNjkyOTQ0NDk3CWI3OGMwOGVjODM1YzE5MjAzYmM2ODlhMGMxZDIxMzAyCQkJd2FuZ3NoYW5nY2hlc2hp; cheshi_user_info_for_index=OTA3OTM3NAlKYXZhRWRnZQl2MgliY2Q2MzFkODQ2ZTE0OGVkMGNlM2U4YTExZGExNmJkMQkxNjkyOTQ0NDk3CWI3OGMwOGVjODM1YzE5MjAzYmM2ODlhMGMxZDIxMzAyCQkJd2FuZ3NoYW5nY2hlc2hp; PHPSESSID=iikkufgki8njel1ue411ictdp1; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Hm_lpvt_8fe47348e12ba11be217fd389b115472=1692945185; pv_cheshit=1692945191085"
cookies = {item.split("=")[0]: item.split("=")[1] for item in cookies.split("; ")}
cookies = requests.utils.cookiejar_from_dict(cookies)

res = requests.get(url, headers=headers, cookies=cookies)

with open("cheshilogin.html", "w") as f:
    f.write(res.text)
