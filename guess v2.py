import random
ans=random.randint(1,20)
i=0
while i<5:
    num=int(input('input a num'))
    if num>ans:
        print('way over')
    elif num<ans:
        print('too less')
    else:
        print('plays',i+1,'times')
        break
    i=i+1