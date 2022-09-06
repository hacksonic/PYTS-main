from msvcrt import LK_UNLCK
import os
from googletrans import Translator
import time
from httpcore import SyncHTTPProxy
import random


font_size='<font size=50>'

proxy_list=[]

with open('E:\h4cksldkflsldlf\Proxy\workproxy.txt', 'r', encoding='utf-8') as p:
    for proxy in p:
        proxy_list.append('http://'+proxy.strip())

    

path='E:\\Udemy\\Tool\\udemy-downloader-master\\out_dir\\100-days-of-code-sub\\'
lecture_list=os.listdir(path)
print(lecture_list)

for lecture in lecture_list:
    srt_list=os.listdir(path+'\\'+lecture)
    for srt_file in srt_list:
        proxy=proxy_list[random.randint(0,len(proxy_list))]

        translator=Translator(proxies=proxy)
        with open(path+'\\'+lecture+'\\'+srt_file, 'r', encoding='utf-8') as f:
            output_file=[]
            output_filename=srt_file.replace('en','zh-tw')
            Line_counting = 0
            for srt_line in f:
                print(srt_line)
                if (Line_counting-2) % 4 == 0:
                    translations=translator.translate(srt_line, dest='zh-tw')
                    output_file.append(font_size+translations.text+ '\n'+font_size+srt_line)
                    print(srt_file)
                else:
                    output_file.append(srt_line)
                time.sleep(1)
                Line_counting += 1

        with open(path+'\\'+lecture+'\\'+output_filename, 'w', encoding='utf-8') as fo:
            for output_line in output_file:
                fo.write(output_line)


# translator = Translator()
# print(translator.translate('안녕하세요.'))
# # <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
# translator.translate('안녕하세요.', dest='ja')
# # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
# translator.translate('veritas lux mea', src='la')
# # <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>


# translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='zh-tw')
# for translation in translations:
#     print(translation.origin, ' -> ', translation.text)
# # The quick brown fox  ->  빠른 갈색 여우
# # jumps over  ->  이상 점프
# # the lazy dog  ->  게으른 개