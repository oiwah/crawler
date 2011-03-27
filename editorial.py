#!/usr/bin/python

import sys
from BeautifulSoup import BeautifulSoup
from urllib import urlopen
import MeCab

f = open('editorial.txt', 'a')
mec = MeCab.Tagger('-Ochasen')
url = "http://www.geocities.jp/ktaro38/rss.xml"
soup = BeautifulSoup(urlopen(url))
titles = soup('title')
texts = soup('description')
for i in range(1, len(titles)):
    f.write(str(titles[i].contents[0]) + '\n')
    text = str(texts[i].contents[0])
    node = mec.parseToNode(text).next
    while node:
        f.write(node.surface + '\t')
        node = node.next
    f.write('\n\n')
