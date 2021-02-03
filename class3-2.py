#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
'''
sports = ['swimming','baseball','basketball','soccer']
print(sports)

sports.append('place')
print(sports)

sports.insert(2,2)
print(sports)

sports.remove(sports[4])
print(sports)
'''
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
'''
stcount = input("How students'math scores you need to count?\n(Enter a number) : ")
scorel = []

for i in range(int(stcount)):
    x = i + 1
    stscore = input('Please enter the score of student{} : '.format(x))
    scorel.append(int(stscore))


hscore = scorel[0]
lscore = scorel[0]

for n in range(len(scorel)):
    if scorel[n] > hscore:
        hscore = scorel[n]
    if scorel[n] < lscore:
        lscore = scorel[n]
        
avescore = sum(scorel)/int(stcount)

print('\n The HIGHEST score in the class is : {}'.format(hscore))
print('\n The LOWEST score in the class is : {}'.format(lscore))
print('\n The AVERAGE score in the class is : {}'.format(avescore))
'''

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#

#---------------------------------------------------------------------------------人數相關#

stcount = input("How many students'math scores you need to count?\n(Enter a number) : ")
scorel = []
stl = []

debugstcount = True  #判斷人數是否為數字
while debugstcount:
    try:
        stcount = int(stcount)
        debugstcount = False
    except:
        stcount =input("\n!!!You must enter a number!!!\nHow many students'math scores you need to count?\n(Enter a number) : ")

#---------------------------------------------------------------------------------名字相關#

nameTF = input('\nDo you want to enter their name? (Yes = 1, No = 2) : ')  #是否要名字

if nameTF == '1':  #輸入名字
    for n in range(int(stcount)):
        x = n + 1
        stname = input('\nPlease enter the NAME of student{}: '.format(x))
        stl.append(stname)
else:
    for n in range(int(stcount)):
        x = n + 1
        stl.append('student{}'.format(x))

#---------------------------------------------------------------------------------分數相關#

hhscore = input('\nPlease enter the FULL SCORE : ')
debughhscore = True

while debughhscore:  #判斷最高分是否為數字
    try:
        hhscore = int(hhscore)
        debughhscore = False
    except:
        hhscore = input('\n!!!You must enter a NUMBER!!!\nPlease enter the FULL SCORE : ')

for s in range(int(stcount)):
    stscore = input('\nPlease enter the SCORE of {}: '.format(stl[s]))

    debugscorenum = True  #判斷分數是否為數字
    while debugscorenum:
        try:
            stscore = int(stscore)
            debugscorenum = False
        except:
            stscore = input('\n!!!You must enter a NUMBER!!!\nPlease enter the SCORE of {}: '.format(stl[s]))

    debugscorerange = True  #判斷分數範圍
    while debugscorerange:
        if stscore <= int(hhscore) and stscore >= 0:
            scorel.append(int(stscore))
            debugscorerange = False
        else:
            stscore = input('\n!!!You must enter a between "0" to "{}"!!!\nPlease enter the SCORE of {}: '.format(hhscore,stl[s]))

def score(scorel):
    hscore = scorel[0]
    lscore = scorel[0]
    
    hscorename = []
    lscorename = []
    
    for l in range(len(scorel)):  #判斷高低分
        if scorel[l] > hscore:
            hscore = scorel[l]
        if scorel[l] < lscore:
            lscore = scorel[l]
    
    for y in range(len(scorel)):  #判斷高低分是誰
        if scorel[y] == hscore:
            hscorename.append(stl[y])
    
        if scorel[y] == lscore:
            lscorename.append(stl[y])
    
    #---------------------------------------------------------------------------------輸出結果#
    
    hstn1 = str(hscorename).strip("[]")
    hstn = str(hstn1).replace("'",'')
    lstn1 = str(lscorename).strip("[]")
    lstn = str(lstn1).replace("'",'')
    
    avescore = sum(scorel)/int(stcount)
    
    print('\n--------------------------------------------------------------')
    if hscore == lscore:
        print("The students all got the same score : {}\nI don't understand why you need to use me".format(hscore))
    else:
        print('\nThe student who got the HIGHEST score in the class is : \n{}\n -- score : {}'.format(hstn,hscore))
        print('\nThe student who got the LOWEST score in the class is : \n{}\n -- score : {}'.format(lstn,lscore))
        print('\nThe AVERAGE score in the class is : {}'.format(avescore))
    input('\n\nEnter any key to EXIT')

score(scorel)

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#

'''

#二維陣列版(未完善，僅能基礎使用)

stcount = input("How students'math scores you need to count?\n(Enter a number) : ")
scorel = []
st = []
sumscore = 0
for i in range(int(stcount)):
    x = i + 1
    stname = input('Please enter the name of student{} : '.format(x))
    st.append(stname)
    stscore = input('Please enter the score of : '.format(st[0]))
    st.append(int(stscore))
    scorel.append(st)
    sumscore += int(stscore)
    st = []
    
#print(scorel)

hname = scorel[0][0]
lname = scorel[0][0]
hscore = scorel[0][1]
lscore = scorel[0][1]

for n in range(len(scorel)):
    if scorel[n][1] > hscore:
        hname = scorel[n][0]
        hscore = scorel[n][1]
    if scorel[n][1] < lscore:
        lname = scorel[n][0]
        lscore = scorel[n][1]
        
avescore = sumscore/int(stcount)

print('\n The HIGHEST score in the class is : {}\n--Name:{}'.format(hscore,hname))
print('\n The LOWEST score in the class is : {}\n--Name:{}'.format(lscore,lname))
print('\n The AVERAGE score in the class is : {}'.format(avescore))

'''

