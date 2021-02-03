
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

stcount = input("How many students'math scores you need to count?\n(Enter a number) : ")
scorel = []
stl = []


debugstcount = True
while debugstcount:
    try:
        stcount = int(stcount)
        debugstcount = False
    except:
        stcount =input("You must enter a number\nHow many students'math scores you need to count?\n(Enter a number) : ")


nameTF = input('Do you want to enter their name? (Yes = 1, No = 2) : ')#是否有名字

if nameTF == '1':#輸入名字
    for n in range(int(stcount)):
        x = n + 1
        stname = input('Please enter the NAME of student{}: '.format(x))
        stl.append(stname)
else:
    for n in range(int(stcount)):
        x = n + 1
        stl.append('student{}'.format(x))


for s in range(int(stcount)):
    stscore = input('Please enter the SCORE of {}: '.format(stl[s]))
    scorel.append(int(stscore))


hscore = scorel[0]
lscore = scorel[0]

hscorename = []
lscorename = []

for l in range(len(scorel)):#判斷高低分
    if scorel[l] > hscore:
        hscore = scorel[l]
    if scorel[l] < lscore:
        lscore = scorel[l]
        
for y in range(len(scorel)):#判斷高低分是誰
    if scorel[y] == hscore:
        hscorename.append(stl[y])
        
    if scorel[y] == lscore:
        lscorename.append(stl[y])
        
hstn1 = str(hscorename).strip("[]")
hstn = str(hstn1).replace("'",'')
lstn1 = str(lscorename).strip("[]")
lstn = str(lstn1).replace("'",'')

        
avescore = sum(scorel)/int(stcount)

print('\n--------------------------------------------------------------')
print('\nThe student who got the HIGHEST score in the class is : \n{}\n -- score : {}'.format(hstn,hscore))
print('\nThe student who got the LOWEST score in the class is : \n{}\n -- score : {}'.format(lstn,lscore))
print('\nThe AVERAGE score in the class is : {}'.format(avescore))