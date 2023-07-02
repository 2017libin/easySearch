import requests
import fire
from urllib.parse import urlparse


def get_domain(subdomain: str) -> list:
    top = ['cn', 'org', 'com', 'edu', 'gov']
    tmp = subdomain.split('.')
    ret = []
    while tmp:
        if tmp[0] not in top and tmp[1] in top:
            ret.append('.'.join(tmp))
        tmp.pop(0)
    return ret


def _google_search_internal(dork: str, start: int, num: int):
    key = ""
    cx = ""
    proxy = {
        'http': '127.0.0.1:7890'
    }
    r = requests.get(f"https://www.googleapis.com/customsearch/v1?key={key}&q={dork}&cx={cx}&start={start}&num={start}",
                     proxies=proxy)
    res = r.json()
    ret = []
    for item in res['items']:
        url = urlparse(item['link'])
        ret.append(f"[*] {item['title']} | {item['link']} | {url.netloc} | {' | '.join(get_domain(url.netloc))}")
    return ret


def googleSearch(input_file: str, output_file: str):
    with open(input_file, "r", encoding="utf-8") as fp:
        for dork in fp:
            try:
                print(f'[+] 搜索 {dork}', end='')
                if dork.strip():
                    ret = _google_search_internal(dork.strip(), 0, 10)
                with open(output_file, "a+", encoding="utf-8") as fp:
                    for line in ret:
                        fp.write(line + '\n')
            except Exception as e:
                print(e)

if __name__ == "__main__":
    fire.Fire(googleSearch)
