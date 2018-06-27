import re
import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

def getCommentCounts(newsurl):
    m = re.search('doc-i(.*).shtml', newsurl)
    newsid = m.group(1)
    commentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-{}&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&thread=1'
    comments = requests.get(commentURL.format(newsid))
    jd = json.loads(comments.text.strip())
    return jd['result']['count']['total']

def getNewDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    result['title'] = soup.select('.main-title')[0].text
    result['newssource'] = soup.select('.date-source a')[0].text
    timesource = soup.select('.date')[0].contents[0].strip()
    result['dt'] = datetime.strptime(timesource,'%Y年%m月%d日 %H:%M')
    result['article'] = ' '.join([p.text.strip() for p in soup.select('#article p')[:-1]])
    result['editor'] = soup.select('.show_author')[0].text.strip('责任编辑:')
    result['comments'] = getCommentCounts(newsurl)
    return result