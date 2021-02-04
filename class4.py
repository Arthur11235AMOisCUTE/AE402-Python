import random

import os

###############################################################################

chnone = '本單字尚未建立中文解釋'
ennone = "The vocabulary hasn't been create an explantion (本單字尚未建立英文解釋)"

dich = {'pass':'跳過','red':chnone,'water':'水'}
dien = {'pass':ennone,
'red':'of the colour of fresh blood',
'water':'a clear liquid, without colour or taste, that falls from the sky as rain and is necessary for animal and plant'}


def reload_dict():
    filech = open('dich.txt','w',encoding = 'UTF-8')
    fileen = open('dien.txt','w',encoding = 'UTF-8')
    
    for k,v in dich.items():
        filech.write(k+':'+v+'\n')
        
    for k,v in dien.items():
        fileen.write(k+':'+v+'\n')
        
    filech.close()
    fileen.close()



if os.path.isfile('dich.txt'):
    filech = open('dich.txt','r',encoding = 'UTF-8')
    for row in filech.readlines():
        data = row.split(':')
        key = data[0]
        value = data[1]
        value = value.strip()
        dich[key] = value
else:
    filech = open('dich.txt','w',encoding = 'UTF-8')
    for k,v in dich.items():
        filech.write(k+':'+v+'\n')


if os.path.isfile('dien.txt'):
    
    fileen = open('dien.txt','r',encoding = 'UTF-8')
    
    for row in fileen.readlines():
        data = row.split(':')
        key = data[0]
        value = data[1]
        value = value.strip()
        
        dien[key] = value
    else:
        fileen = open('dien.txt','w',encoding = 'UTF-8')
        for k,v in dien.items():
            fileen.write(k+':'+v+'\n')

filech.close()
fileen.close()



###############################################################################

print('\n#----------------------------------#')
print('歡迎來到本字典')
print('#----------------------------------#')
print('\n本字典功能如下')


onoff = True
choose = '0'


while onoff:

###############################################################################

    if choose == '0':
        print('\n@#$&% 功能表 %&$#@')
        print('--')
        print('0. 叫出功能表')
        print('1. 收錄新單字/建立解釋')
        print('2. 列出已收錄字彙表')
        print('3. 刪除所有已收錄字彙')
        print('4. 移除單字')
        print('5. 鍵入英文執行翻譯(中 + 英)')
        print('6. 中翻英')
        print('7. 小測驗')
        print('8. 回復預設值')
        print('9. 離開本典')
        
        choose = input('\n請輸入欲執行功能代碼 ')

###############################################################################

    elif choose == '1' :
        print('\n收錄新單字/建立解釋\n')
        key = input('請輸入欲建立之英文單字 (鍵入0可跳出本功能) : ')
        
        if key == '0':
            choose = '0'
            
        else:
            
            if (key in dich and dich[key] == chnone) or not key in dich:
                valuech = input('請輸入 {} 之中文解釋 (鍵入pass0可跳過) : '.format(key))
            else:
                print('本單字" {} "已有中文解釋 --{}\n若需更改解釋請移除該單字後重新建立'.format(key,dich[key]))
                valuech = dich[key]
                
            if (key in dien and dien[key] == ennone) or not key in dien:
                valueen = input('請輸入 {} 之英文解釋 (鍵入pass0可跳過) : '.format(key))
            else:
                print('本單字" {} "已有英文解釋 --{}\n若需更改解釋請移除該單字後重新建立'.format(key,dien[key]))
                valueen = dien[key]
                
            
            if valuech == 'pass0':
                dich[key] = chnone
            else:
                dich[key] = valuech
            
            if valueen == 'pass0':
                dien[key] = ennone
            else:
                dien[key] = valueen
            
            reload_dict()

###############################################################################

    elif choose == '2':
        print('\n列出已收錄字彙表')
        for key in dich.keys():
            print('\n{}\n-{}\n-{}\n'.format(key,dich[key],dien[key]))
        if dich == {}:
            print('\n字彙表空空如也，鍵入1可建立字彙表')
        choose = input('鍵入0可跳出本功能 ')

###############################################################################

    elif choose == '3':
        print('\n刪除所有已收錄字彙\n')
        tf = False
        asktf = input('確認要刪除所有已收錄字彙嗎? (1 : Yes / 2 : No) : ')
        if asktf == '1':
            tf = True
        if tf:
            dich = {}
            dien = {}
            
            reload_dict()
            
            print('已收錄字彙已全數刪除 (鍵入2可列出字彙表)')
            choose = input('鍵入0可跳出本功能 ')
        else:
            choose = '0'

###############################################################################

    elif choose == '4':
        print('\n移除單字\n')
        delkey = input('請鍵入欲刪除之單字 : ')
        
        if delkey in dich:
            tf = False
            asktf = input('確認要刪除 " {} " 嗎? (1 : Yes / 2 : No) : '.format(delkey))
            if asktf == '1':
                tf = True
            if tf:
                dich.pop(delkey)
                dien.pop(delkey)
                
                reload_dict()
                
                print('已刪除 " {} " (鍵入2可列出字彙表)'.format(delkey))
                choose = input('鍵入0可跳出本功能 ')
        else:
            print('該字 " {} " 未收錄於本字典'.format(delkey))

###############################################################################

    elif choose == '5':
        print('\n鍵入英文執行翻譯(中 + 英)\n')
        voc = input('請鍵入欲查詢之英文單字 (鍵入0可跳出本功能) : ')
        if voc == '0':
            choose = '0'
        else:
            if voc in dich:
                print('\n該單字 " {} " 之中文解釋為 \n--{}'.format(voc,dich[voc]))
                print('該單字 " {} " 之英文解釋為 \n--{}'.format(voc,dien[voc]))
            else:
                print('\n該單字 " {} " 尚未被建立於本典'.format(voc))

###############################################################################

    elif choose == '6':
        print('\n中翻英\n')
        got = False
        ch = input('請鍵入欲查詢之中文 (鍵入0可跳出本功能) : ')
        if ch == '0':
            choose = '0'
        else:
            for k,v in dich.items():
                if v == ch:
                    print('該單字 " {} " 之英文解釋為 \n--{}'.format(ch,dien[k]))
                    got = True
            if not got:
                print('無法將 " {} " 翻譯成英文(未收錄於本典)'.format(ch))

###############################################################################

    elif choose == '7':
        print('\n小測驗')
        score = 0
        tf = input('\n鍵入start開始測驗 (鍵入0可跳出本功能) : ')
        
        if tf == '0':
            choose = '0'
        elif tf == 'start':
            testl = []
            for k,v in dich.items():
                if not v == chnone:
                    testl.append(v)
            for k,v in dien.items():
                if not v == ennone:
                    testl.append(v)
            
            if len(testl) >= 20 :
                testlen = 20
            else:
                testlen = len(testl)
            
            print('\n測驗開始\n\n本測驗共有{}題'.format(testlen))
            
            for i in range(testlen):
                got = False
                x = i + 1
                lnum = random.randrange(len(testl))
                uans = input('\n第{}題\n請鍵入 " {} " 該釋義之英文單字 : '.format(x,testl[lnum]))
                for k,v in dich.items():
                    if v == testl[lnum]:
                        if uans == k:
                            score += 1
                            ans = k
                            got = True
                for k,v in dien.items():
                    if v == testl[lnum]:
                        if uans == k:
                            score += 1
                            ans = k
                            got = True
                if got:
                    print('你答對了!\n正確答案為 " {} " \n目前分數 {}/{}'.format(ans,score,testlen))
                else:
                    print('你答錯了!\n正確答案為 " {} " \n目前分數 {}/{}'.format(ans,score,testlen))
                testl.remove(testl[lnum])
            print('\n測驗結束\n你一共獲得 {} 分\n恭喜!!'.format(score))

###############################################################################

    elif choose == '9':
        print('Bye-bye\n我們下次見')
        break

###############################################################################

    elif choose == '8':
        print('\n回復初始值\n')
        tf = False
        asktf = input('確認要回復初始值嗎? (1 : Yes / 2 : No) : ')
        if asktf == '1':
            tf = True
        if tf:
            dich = {'pass':'跳過','red':chnone,'water':'水'}
            dien = {'pass':ennone,
                    'red':'of the colour of fresh blood',
                    'water':'a clear liquid, without colour or taste, that falls from the sky as rain and is necessary for animal and plant'}
            
            reload_dict()
            
            print('已回復初始值 (鍵入2可列出字彙表)')
            choose = input('鍵入0可跳出本功能 ')
        else:
            choose = '0'

###############################################################################

    else:
       choose = input('輸入錯誤，請重新輸入 (鍵入0可叫出功能表) : ')
        
