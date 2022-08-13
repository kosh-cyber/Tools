import requests

header = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "cookie": "prov=5cc1c3ee-28da-21fe-3cd0-7c1418402562; _ga=GA1.2.547003135.1642140964; OptanonAlertBoxClosed=2022-03-08T23:00:34.784Z; OptanonConsent=isIABGlobal=false&datestamp=Wed+Mar+09+2022+07%3A00%3A34+GMT%2B0800+(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)&version=6.10.0&hosts=&landingPath=NotLandingPage&groups=C0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0001%3A1; __gads=ID=42182d93c00fa751:T=1648561569:S=ALNI_MaDFtPlbNuxuZUgxPbi9tIQD5Tafw; __gpi=UID=000004eb5c4c5a58:T=1650347530:RT=1651996799:S=ALNI_MYrKq1JBE1-LUrH2B-yPG3rnj0wlw; _gid=GA1.2.1639692247.1660310674; _gat=1",
    "referer": "https://www.google.com/",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "cross-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }

def pretty_print_POST(req):
    r_r = '{}\r\n{}\r\n\r\n{}'.format(req.method + ' ' + req.url,'\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),req.body)
    return r_r.replace('\r\n', "\n")
req = requests.Request('POST','https://stackoverflow.com/questions/17309288/importerror-no-module-named-requests',headers=header,data='FUZZ')
prepared = req.prepare()
path = '\\\\127.0.0.1\\c$\\Users\\\\Desktop\\httprequest.txt'
with open(path, 'w+') as f:
        f.writelines(pretty_print_POST(prepared))
