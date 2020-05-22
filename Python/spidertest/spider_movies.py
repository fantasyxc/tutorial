import requests
from bs4 import BeautifulSoup
import re
import time

moviekeywords = ['李采潭', '高颜值']

def crawl_poxiao():

    poxiao_url = "https://www.poxiao.com/"
    poxiao_headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        'upgrade-insecure-requests': '1',

    }
    poxiao_req = requests.get(poxiao_url, headers = poxiao_headers)
    #print(poxiao_req.content)
    poxiao_soup = BeautifulSoup(poxiao_req.content)
    moviecontent = poxiao_soup.find(id="indextopleft")

    print(moviecontent)

    #moviecontent = moviecontent[]


def craw_btjiaindex():
    url = "http://www.btbtt01.com/"
    headers = {
        'Host': 'www.btbtt01.com',
        #'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    }

    req = requests.get(url, headers = headers)

    soup = BeautifulSoup(req.content)
    #moviecontentbox = soup.find(id='threadlist')
    #print(moviecontentbox)


    moviecontent = soup.findAll('a', {'class':'subject_link'})
    for movie in moviecontent:
        print(movie)
        #print(movie.get('text'))
        #print(movie.get('href'))


    '''
    movietable = soup.findAll('table', {'class':'thread'})
    for movie in movietable:
        print("="*50)
        print(movie)
    '''


'''
crwa btjia url by type
'''
def craw_btjia_type(url):
    headers = {
        'Host': 'www.btbtt01.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    }

    movielistreq = requests.get(url, headers=headers)
    movielistsoup = BeautifulSoup(movielistreq.content)

    movielists = movielistsoup.findAll('a', {'class':'subject_link'})
    for movielist in movielists:
        movielisttext = movielist.text
        # get movie url
        for moviekeyword in moviekeywords:
            if (moviekeyword in movielisttext):
                movieurl = movielist.get('href')
                print("text: %s \nurl: %s" % (movielisttext, movieurl))
                print("-" * 80)

        # #get image
        # moviereq = requests.get(movieurl, headers=headers)
        # print(moviereq.content)
        # moviesoup = BeautifulSoup(moviereq.content)
        #
        # # find all image url
        # moiveimglists = moviesoup.findAll('img')
        # for movieimg in moiveimglists:
        #     print("image: %s" % movieimg)
        #     #print(movieimg['src'])
        #break

if __name__ == "__main__":
    print("Korea:")
    urlkorea = ""
    urljapan = ""

    with open('lagou.json', 'w') as fp:
        fp.write(line.encode('utf-8'))
    for pagekorea in range(1, 39):
        # generate url
        urlkorea = "http://www.btbtt01.com/forum-index-fid-1-typeid1-2-typeid2-0-typeid3-0-typeid4-0-page-%d.htm" % pagekorea

        # craw url
        craw_btjia_type(urlkorea)

        time.sleep(5)

    print("Japan")
    for pagejapan in range(1, 32):
        urljapan = "http://www.btbtt01.com/forum-index-fid-1-typeid1-8-typeid2-0-typeid3-0-typeid4-0-page-%d.htm" % pagejapan
        craw_btjia_type(urljapan)
        time.sleep(5)