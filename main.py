page=0
flag0=0 #pen or no pen
flag1=0
flag1a=0 #sword or no sword
flag2=0
flag2a=0

def end():
    print('\n \n \n THE END\n \n \n')
    exit()

class quick:
    def inp(type=str):
        inp = type(input(' >> '))
        return inp

    def readPage(load):
        pg = open('./pages/'+str(load)+'.txt')
        print(pg.read())

    def cont(pg, pgNum=1):
        input(' (Press Enter to continue) ')
        pg = pg + pgNum
        return pg

    def act(choice1, choice2, choice3='', choice4=''):
        print('(1) '+choice1)
        print('(2) '+choice2)
        if choice3 == '':
            choice = quick.inp(int)
            return choice
        elif choice4 == '':
            print('(3) '+choice3)
            choice = quick.inp(int)
            return choice
        else:
            print('(3) '+choice3)
            print('(4) '+choice4)
            choice = quick.inp(int)
            return choice



print('Welcome to the Timespace Chronicals')

print('(1) Start \n'+'(2) Continue')
choice = 0

while choice != 1 or 2:
    choice = quick.inp(int)
    if choice == 1:
        page = 1
        break
    elif choice == 2:
        print('Which page are you on?')
        page = quick.inp(int)
        break
    else:
        print('Invalid choice!!')
        continue


quick.readPage(page) #page 1
page = quick.cont(page)
quick.readPage(page) #page 2


flag0 = quick.act("Why would I need a pen? (Don't take pen)", "Why not? (Take the pen)")

while flag0 != 1 or 2:
    if flag0 == 1:
        page = 3
        break
    elif flag0 == 2:
        page = 7
        break
    else:
        print("Invalid Choice!!")
        flag0 = quick.act("Why would I need a pen? (Don't take pen)", "Why not? (Take the pen)")
        continue

if flag0 == 1:
    quick.readPage(page) #page 3
    page = quick.cont(page)
    quick.readPage(page) #page 4
    page = quick.cont(page)
    quick.readPage(page) #page 5
    page = quick.cont(page)
else:
    quick.readPage(page) #page 7
    page = quick.cont(page)
    quick.readPage(page) #page 8
    page = quick.cont(page)
    quick.readPage(page) #page 9
    page = quick.cont(page)

page = 6
quick.readPage(page) #page 6
page = 10
quick.readPage(page) #page 10

# I was being retarded while formatting the first couple of pages but I can't be fucked to go back and redo it

page = quick.cont(page)
quick.readPage(page) #page 11
page = quick.cont(page)
quick.readPage(page) #page 12

flag1 = quick.act("Go Left", "Go Right")

#Hallway Prompt
while flag1 != 1 or 2:
    if flag1 == 1:
        page = 17
        quick.readPage(page) #page 17
        page = 18
        break
    elif flag1 == 2:
        page = 13
        break
    else:
        print("Invalid Choice!!")
        flag1 = quick.act("Go Left", "Go Right")
        continue

if flag1 == 2:
    quick.readPage(page) #page 13
    flag1a = quick.act("Take it", "Do not")
    #Take da sword prompt

    while flag1a != 1 or 2:
        if flag1a == 1:
            page = 14
            quick.readPage(page)
            break
        elif flag1a == 2:
            page = 15
            quick.readPage(page)
            break
        else:
            print("Invalid Choice!!")
            flag1a = quick.act("Take it", "Do not")
            continue
    page = 16
    quick.readPage(page) #page 16
    page = quick.cont(page)
    page = 18

quick.readPage(page) #page 18
page = quick.cont(page)
quick.readPage(page) #page 19


flag2 = quick.act("Hide behind the wall", "Attack the Figure", "Wait to see what happens")

#Hallway Prompt
while flag2 != 1 or 2 or 3:
    if flag2 == 1:
        page = 20
        quick.readPage(page)
        page = 26
        break
    elif flag2 == 2:
        page = 21
        quick.readPage(page)
        break
    elif flag2 == 3:
        print('You stand perfectly still, staring at the monster, it turns to stare back.')
        print('\nAfter a few seconds of a staring contest, it rushes you down.  \n \n You get impaled on the monster spiky arm and die')
        end() ###  you absolute idiot
    else:
        print("Invalid Choice!!")
        flag2 = quick.act("Go Left", "Go Right")
        continue

if flag2 == 2:
    if flag0 == 2 and flag1a == 1:
        print('What do you want to attack with? \n \n')
        flag2a = quick.act("Attack with the Pen", "Attack with the Sword")
        while flag2a != 1 or 2:
            if flag2a == 1:
                print('You attack with the Pen. \n')
                page = 22
                break
            elif flag2a == 2:
                page = 00
                break
            else:
                print("Invalid Choice!!")
                flag2a = quick.act("Attack with the Pen", "Attack with the Sword")
                continue
    elif flag0 == 2 and flag1a == 2:
        print('Being your only viable weapon, you attack with the Pen. \n')
        page = 22
    elif flag0 == 1 and flag1a == 1:
        print('Being your only viable weapon, you attack with the Sword. \n')
        page = 24
    else:
        print('Stupidly, you rush forward, weaponless, and attack the monster. \n \n You get impaled on the monster spiky arm and die')
        end()

quick.readPage(page) #This can be a couple of pages
page = 26
quick.readPage(page) #page 26
page = 27
quick.readPage(page) #page 27