import requests
from bs4 import BeautifulSoup

def crawl_detail(id):
    url = "https://www.lagou.com/jobs/%s.html" % id
    headers = {
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    }
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content)
    jobbt = soup.find('dd', attrs={'class':'job_bt'})
    print(jobbt)


def main():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': None,
        'X-Requested-With': 'XMLHttpRequest'
    }

    form_data = {
        'first': 'true',
        'pn': '1',
        'kd': 'python'
    }
    result = requests.post("https://www.lagou.com/jobs/positionAjax.json?city=%E6%AD%A6%E6%B1%89&needAddtionalResult=false", headers=headers, data=form_data)

    json_result = result.json()
    print(json_result)
    positions = json_result['content']['positionResult']['result']

    #line = json.dump(positions, ensure_ascii=False)
    #with open('lagou.json', 'w') as fp:
    #    fp.write(line.encode('utf-8'))


if __name__ == '__main__':
    main()