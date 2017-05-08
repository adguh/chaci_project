import json
import sys
import sqlite3
import webbrowser
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def command_description():       
    print('************命令说明************\n')
    print('输入 word 单词  查询单词\n')
    print('输入 record     用浏览器查看单词查询历史记录\n')
    print('输入 export     导出单词查询历史记录到d:\\word_list.txt文件中\n')
    print('输入 quit       退出查词程序\n')


def translation(word):    
    content=word
    url='http://fanyi.youdao.com/openapi.do?keyfrom=chacitranslation&key=1214752623&type=data&doctype=json&version=1.1&q='
    response = urllib.request.urlopen(url+content)
    html = response.read().decode('utf-8')
    s = json.loads(html)
    t = s.get('basic').get('explains')
    for i in t:
        print(i)
    save(word)


def save(word):
    content = word
    url = "http://127.0.0.1:8000/check_word/add?word="
    response = urllib.request.urlopen(url + content)


def show():
    sys.path.append ("libs")
    url = "http://127.0.0.1:8000/check_word/"
    webbrowser.open(url)
    print('单词查询历史记录已显示在浏览器中')


def export():
    url = "http://127.0.0.1:8000/check_word/"
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html,'html.parser')
    result = []
    for i in soup.findAll('td'):
        result.append(i.string.split(' ')[0])
    f = open('d:/word_list.txt','w')
    for word in result:
        f.write('%s\n' % word)
    f.close()
    print('单词查询历史记录已导出到d:\\word_list.txt文件中')


command_description()
while True:
    msg = input('请输入命令：\n')
    if msg == 'quit':
        break
    elif msg == 'record':
        show()
    elif msg == 'export':
        export()
    else:
        [order, word] = msg.split(' ')
        if order == 'word':
            translation(word)



