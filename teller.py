import sys
import time
import sqlite3
import re
import traceback
import telepot
from pprint import pprint
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import parse

class Telegram:
    def __init__(self):
        self.bot = telepot.Bot('1894072938:AAE54zG8gITUFBVF7-PnwKXp1vrugaNtG68')
        self.bot.getMe()
        self.id = 1874023304
        self.key = "YrQn72lYE4qA3NfS2pkl%2FEwy95kCZ8jghF27PMOoOD3apbMi6htMwfFztU28urc6rMLLh8eWyVdDGVLCooMWPw%3D%3D"
        #self.key_2 ="YrQn72lYE4qA3NfS2pkl%2FEwy95kCZ8jghF27PMOoOD3apbMi6htMwfFztU28urc6rMLLh8eWyVdDGVLCooMWPw%3D%3D"
        self.bot.sendMessage(self.id, '내정신좀보소 bot 입니다.')
        self.bot.message_loop(self.handle)
        print('Listening...')
        while 1:
            time.sleep(10)

    def replyData(self,data_param,area,object):
        if data_param ==0:
            url = 'http://apis.data.go.kr/1320000/LosfundInfoInqireService/getLosfundInfoAccToLc?serviceKey=' + self.key + \
                  '&PRDT_NM='+str(parse.quote(object)) +'&ADDR='+str(parse.quote(area)) +'&pageNo=1&numOfRows=10'
        elif data_param ==1:
            url = 'http://apis.data.go.kr/1320000/LostGoodsInfoInqireService/getLostGoodsInfoAccTpNmCstdyPlace?serviceKey=' + self.key + \
                  '&LST_PLACE='+str(parse.quote(area)) +'&LST_PRDT_NM='+str(parse.quote(object)) +'&pageNo=1&numOfRows=10'

        response = urlopen(url).read()

        soup = BeautifulSoup(response, 'html.parser')
        items = soup.findAll('item')
        res_list = []
        for item in items:
            sItem = str(item)
            item = re.sub('<.*?>', '|', sItem)
            parsed = item.split('|')
            print(parsed)
            try:
                if data_param ==0:
                    row = parsed[2] + '\n' + parsed[6] + '\n' + parsed[10] + '\n' + parsed[14] + '\n  '
                elif data_param ==1:
                    row = parsed[4] + '\n' + parsed[8] + '\n' + parsed[10] + '\n'

            except IndexError:
                row = item.replace('|', ',')
            if row:
                res_list.append(row.strip())
        msg = ' '
        for r in res_list:
            if len(r + msg) + 1 > 300:
                msg += r + '\n'
            else:
                msg += r + '\n'
        if msg:
            self.bot.sendMessage(self.id, msg)
        else:
            self.bot.sendMessage(self.id, '데이터가 없습니다')

    def handle(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type != 'text':
            self.bot.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
            return

        text = msg['text']
        args = text.split(' ')
        if text.startswith('분실') and len(args)>1:
            print('try to 분실',args[1])
            self.replyData(1,args[1],args[2])
        elif text.startswith('습득') and len(args)>1:
            print('try to 습득', args[1])
            self.replyData(0,args[1],args[2])
        else:
            self.bot.sendMessage(chat_id, '모르는 명령어입니다.\n분실 또는 습득 지역 물건종류 순서로 입력하세요.')


Telegram()