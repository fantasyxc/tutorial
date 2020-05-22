import requests
from bs4 import BeautifulSoup
import sys
import io
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

'''
crwa btjia url by type
'''
def craw_btjia_type(url, headers, fp, keywords):
    movielistreq = requests.get(url, headers=headers)
    movielistsoup = BeautifulSoup(movielistreq.content)

    movielists = movielistsoup.findAll('a', {'class':'subject_link'})
    for movielist in movielists:
        movielisttext = movielist.text
        for moviekeyword in keywords:
            if (moviekeyword in movielisttext):
                movieurl = movielist.get('href')    # get movie url
                #linestr = "text: %s \nurl: %s" % (movielisttext, movieurl)
                linestr = "- [%s](%s)\n" % (movielisttext, movieurl)
                fp.write(linestr)


if __name__ == "__main__":
    urlindex= "http://www.btbtt01.com/forum-index-fid-1-page-1.htm"
    #urlkorea = "http://www.btbtt01.com/forum-index-fid-1-typeid1-2-typeid2-0-typeid3-0-typeid4-0.htm"
    #urljapan = "http://www.btbtt01.com/forum-index-fid-1-typeid1-8-typeid2-0-typeid3-0-typeid4-0.htm"
    headers = {
        'Host': 'www.btbtt01.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    }
    #maxpage = 16
    maxpageall = 380
    filenameall = 'movielist-all.md'
    #filenamekorea = 'movielist-korea.md'
    #filenamejapan = 'movielist-japan.md'
    moviekeywordsall = ['李采潭', '颜值', '极品', '身材', '三男两女', '3P']
    #moviekeywordskorea = ['李采潭', '颜值', '漂亮', '性感', '极品', '身材', '劲爆', '必看', '职场', '三男两女', '3P']

    with open(filenameall, 'w') as fpall:
        print("All:")
        for pageall in range(1, maxpageall):
            print("page:%d" % pageall)
            print("-" * 100)
            urlall = "http://www.btbtt01.com/forum-index-fid-1-page-%d.htm" % pageall
            craw_btjia_type(urlall, headers, fpall, moviekeywordsall)
            #time.sleep(5)

    # with open(filenamekorea, 'w') as fpkorea:
    #     print("Korea:")
    #     for pagekorea in range(1, maxpage):
    #         print("page:%d" % pagekorea)
    #         print("-" * 100)
    #         urlkorea = "http://www.btbtt01.com/forum-index-fid-1-typeid1-2-typeid2-0-typeid3-0-typeid4-0-page-%d.htm" % pagekorea
    #         craw_btjia_type(urlkorea, headers, fpkorea, moviekeywordskorea)
    #         time.sleep(5)
    #
    # with open(filenamejapan, 'w') as fpjapan:
    #     print("Japan:")
    #     for pagejapan in range(1, maxpage):
    #         print("page:%d" % pagejapan)
    #         print("-" * 100)
    #         urljapan = "http://www.btbtt01.com/forum-index-fid-1-typeid1-8-typeid2-0-typeid3-0-typeid4-0-page-%d.htm" % pagejapan
    #         craw_btjia_type(urljapan, headers, fpjapan, moviekeywordskorea)
    #         time.sleep(5)

