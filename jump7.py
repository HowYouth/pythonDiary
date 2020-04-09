#print('Do not print contains 7 or 7 Times,0-100')
a=0
b=int(a)
c=0
while b<=100:
    if b%7==0: #7 de beishu bu shuchu
        #print('pass')
        pass
    elif b%10==7: # gewei wei 7 bu shuchu
        #print('pass')
        pass
    elif b//10%10==7: #shiwei wei 7 bu shuchu
        #print('pass')
        pass
    else:
        print(b)
        c+=1
    b+=1
#print('OVER! TOTAL: {}'.format(c))

