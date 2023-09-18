import execjs
import requests
#
# headers = {
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Cache-Control': 'no-cache',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'DNT': '1',
#     'Origin': 'https://www.qimingpian.com',
#     'Pragma': 'no-cache',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'cross-site',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
# }
#
# data = {
#     'page': '1',
#     'num': '20',
#     'sys': 'vip',
#     'keywords': '',
#     'unionid': '',
# }
#
# response = requests.post('https://vipapi.qimingpian.cn/search/recommendedItemList', headers=headers, data=data).json()
# encrypt_data = response['encrypt_data']
#
# data123 = open('./demo.js', 'r', encoding='utf-8').read()
#
# ctx = execjs.compile(data123).call('s', encrypt_data)
# print(ctx)

import requests

cookies = {
    'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a': '1693837580',
    'SL_G_WPT_TO': 'zh',
    'SL_GWPT_Show_Hide_tmp': '1',
    'SL_wptGlobTipTmp': '1',
    '__g': '-',
    '__zp_seo_uuid__': 'b7148196-8805-454f-b731-06f40130943f',
    '__l': 'r=https%3A%2F%2Fwww.google.com.hk%2F&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Frecommend&s=1&s=3&friend_source=0',
    'wd_guid': '87da6dad-b0de-4740-b21e-38cd508c0b76',
    'historyState': 'state',
    '_bl_uid': '6qlIpmw3k6hg2m7wwuU8oXn56qCI',
    'boss_login_mode': 'wechat',
    'wt2': 'DSZcZfDko8ToCM1FWXJXyxYpmzWc6qC7DYF_pPVBN1yy5DhT0pZmhzkj59j_q8S8tHe4iKb1A3JcfGhjd5Y8-ww~~',
    'wbg': '0',
    'lastCity': '101010100',
    'Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a': '1694773286',
    '__c': '1693837584',
    '__a': '69506831.1693837584..1693837584.12.1.12.12',
    'geek_zp_token': 'V1QtwvF-T001dgXdNgyxofKiOz7TrVxQ~~',
    '__zp_stoken__': 'f9a3eaT9VaHlGN2YzED8gOCE6AQQkKFxBMUtAPwsCXw57GhNkMVBGIzo0XXYwGSo8Fx8JcTAlN35sSUoAYWsZRDxQJhtdBDc5QSADT0EFMxwueE02IRISOFpTGCh1Hnt3VSY7Dj9EXVVyeTk%3D',
}

headers = {
    'authority': 'www.zhipin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1693837580; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; __g=-; __zp_seo_uuid__=b7148196-8805-454f-b731-06f40130943f; __l=r=https%3A%2F%2Fwww.google.com.hk%2F&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Frecommend&s=1&s=3&friend_source=0; wd_guid=87da6dad-b0de-4740-b21e-38cd508c0b76; historyState=state; _bl_uid=6qlIpmw3k6hg2m7wwuU8oXn56qCI; boss_login_mode=wechat; wt2=DSZcZfDko8ToCM1FWXJXyxYpmzWc6qC7DYF_pPVBN1yy5DhT0pZmhzkj59j_q8S8tHe4iKb1A3JcfGhjd5Y8-ww~~; wbg=0; lastCity=101010100; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1694773286; __c=1693837584; __a=69506831.1693837584..1693837584.12.1.12.12; geek_zp_token=V1QtwvF-T001dgXdNgyxofKiOz7TrVxQ~~; __zp_stoken__=f9a3eaT9VaHlGN2YzED8gOCE6AQQkKFxBMUtAPwsCXw57GhNkMVBGIzo0XXYwGSo8Fx8JcTAlN35sSUoAYWsZRDxQJhtdBDc5QSADT0EFMxwueE02IRISOFpTGCh1Hnt3VSY7Dj9EXVVyeTk%3D',
    'dnt': '1',
    'pragma': 'no-cache',
    'referer': 'https://www.zhipin.com/web/geek/job?city=101020100&experience=105',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'token': 'Vhq7OxqsJ52oFaH',
    'traceid': '036563F4-271F-4D4F-A4BB-C3288A0D9F2F',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'zp_token': 'V1QtwvF-T001dgXdNgyxofKiOz7TrVxQ~~',
}

params = {
    'scene': '1',
    'query': '',
    'city': '101020100',
    'experience': '105',
    'payType': '',
    'partTime': '',
    'degree': '',
    'industry': '',
    'scale': '',
    'stage': '',
    'position': '',
    'jobType': '',
    'salary': '',
    'multiBusinessDistrict': '',
    'multiSubway': '',
    'page': '1',
    'pageSize': '30',
}

response = requests.get('https://www.zhipin.com/wapi/zpgeek/search/joblist.json', params=params, cookies=cookies, headers=headers).json()
jobList = response['jobList']

data123 = open('./demo.js', 'r', encoding='utf-8').read()

ctx = execjs.compile(data123).call('s', encrypt_data)
print(ctx)