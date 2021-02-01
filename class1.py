'import time'

'''
print("I'm Eric")
print('He is "cool"')
'''

'''
name = input('Who are you? (Please enter your name) : ')
print('Hi! {} ~ How are you today~/n/n'.format(name))
'''

'''
r = input('Enter the radius about the circle : ')

pi = (3.141592653589793)

a = ((float(r)**2)*pi)

l = (2*(float(r))*pi)

print('This is the radius that you want to know about the circle     : {}'.format(r))

print('This is the perimeter that you want to know about the circle  : {}'.format(l))

print('This is the area that you want to know about the circle       : {}'.format(a))
'''

'''
s = input('Enter your score : ')

if int(s) > 100:
    print('Are you kidding me?????????')
elif int(s) >= 60:
    print('PASS   (score : {})'.format(s))
else:
    print('FAIL   (score : {})'.format(s))
'''

s = input('Enter your score : ')

if int(s) > 100 or int(s) < 0:
    input('Are you kidding me?????????\nThe score must between 0-100\n\nEnter your score : ')
elif int(s) >= 90:
    print('PASS level[A]  (score : {})'.format(s))
elif int(s) >= 80:
    print('PASS level[B]  (score : {})'.format(s))
elif int(s) >= 70:
    print('PASS level[C]  (score : {})'.format(s))
elif int(s) >= 60:
    print('PASS level[D]  (score : {})'.format(s))
else:
    print('FAIL level[F]  (score : {})'.format(s))
