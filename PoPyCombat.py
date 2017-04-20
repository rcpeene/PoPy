#PoPyCombat.py by Ross Peene

#https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-
#programming/
#http://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-1-items-and-enemies/
#http://blog.trinket.io/python-text-adventure/

#Norman's Sword, Norman's Dagger, Norman's Bow, Paragon Blade, Halfdan, Sycamore

#CURRENT GOALS:
#Implement duel-equipping/Limit two-handed weapon equipping
#Reimplement command input
#Implement weapon ammo
#Check/Implement other weapon properties [versatile,thrown,reach,etc.]
#Implement adjacent field item locations and random field item locations into createfield
#Design various item subclasses [potion,chest,armor,etc.]

from time import sleep
from random import randint
from math import floor,sqrt

test = "test"
laughter = "HAHAHAHAHA!"
options = "[options_list_sample]"
combatoptions = "attack: Use a weapon to attack a target." +\
                "\ncast: Cast a spell. " +\
                "\ndash: Use your major action to double your movement." +\
                "\ndisengage: Your movement will not provoke any opportunity attacks for the " +\
                "rest of your turn." +\
                "\ndodge: Any attack on you has disadvantage for the rest of your turn." +\
                "\nhide: You make a stealth check against the creature(s) you wish to hide, " +\
                "against their passive perception. If you succeed, their attacks on you have " +\
                "disadvantage, and your attacks on them have advantage." +\
                "\nready: Forgo your turn so that you may act when a specific event happens." +\
                "\nequip: Equip a weapon."

creaturedesc = {"bat":"A vicious bat.",
                "beholder":"A large, spherical monstrosity with eleven eyes that shoot magical " +
                "rays.",
                "reddragon":"A massive adult winged, fire-breathing, dragon."}

weapondesc = {"sword":"A simple iron sword.",
              "bow":"A simple wooden bow.",
              "dagger":"A small sharp blade.",
              "unarmed":"An emptyhanded attack."}

def diceroll(n,d,m):
    x = 0
    for roll in range(0,n):
        x = x + randint(1,d)
    x = x + m
    return x
    
def advantage(n,d,m):
    return max(diceroll(n,d,m),diceroll(n,d,m))
    
def disadvantage(n,d,m):
    return min(diceroll(n,d,m),diceroll(n,d,m))

def gameover():
    sleep(1)
    print()
    print("GAME OVER")
    while True:
        sleep(100000)

def checkyesno(command):
    if command in ["y","ye","ya","yes","yup","yeah","yea","ok","okay","sure","aye","indeed",
                   "affirmative","si","ja"]:
        return True
    elif command in ["n","no","nope","nah","nay","negative","negatory","nein"]:
        return False
    else:
        return

def checkadj(loc1,loc2):
    if loc1[0] == loc2[0] and loc1[1] == loc2[1]:
        return True
    elif loc1[0] + 1 == loc2[0] or loc1[0] - 1 == loc2[0]:
        return True
    elif loc1[1] - 1 == loc2[1] or loc1[1] + 1 == loc2[1]:
        return True
    else:
        return False

def checkcommand(command):
    if command in ["o","opt","ops","option","options"]:
        print(options)
        sleep(2)
    if command in ["laugh","laughter","ha","hah","haha"]:
        print(laughter)
        sleep(2)
    else:
        return False

class item():
    def __init__(self,name,value,weight,desc,loc):
        self.name = name
        self.value = value
        self.weight = weight
        self.loc = loc

    def __repr__(self):
        return '{}'.format(self.name)

class weapon(item):
    def __init__(self,name,desc,value,n,d,m,dmg,ammunition,finesse,heavy,light,loading,ranged,
                 reach,thrown,twohanded,versatile):
        self.name = name
        self.desc = desc
        self.value = value
        self.n = n
        self.d = d
        self.m = m
        self.dmg = dmg
        self.ammunition = ammunition
        self.finesse = finesse
        self.heavy = heavy
        self.light = light
        self.loading = loading
        self.ranged = ranged
        if type(self.ranged) == list:
            self.shortrange = self.ranged[0]
            self.longrange = self.ranged[1]
        else:
            self.shortrange = 0
            self.longrange = 0
        self.reach = reach
        self.thrown = thrown
        self.twohanded = twohanded
        self.versatile = versatile

class player():
    def __init__(self,name,race,size,clss,xp,ac,hp,maxhp,speed,Str,Dex,Con,Int,Cha,Wis,wep1,wep2,
                 proflist):
        self.name = name
        self.size = size
        self.ac = ac
        self.hp = hp
        self.maxp = maxhp
        self.speed = speed
        self.str = Str
        self.dex = Dex
        self.con = Con
        self.int = Int
        self.cha = Cha
        self.wis = Wis
        self.clss = clss
        self.xp = xp
        self.wep1 = wep1
        self.wep2 = wep2
        self.strmod = self.getmod(Str)
        self.dexmod = self.getmod(Dex)
        self.conmod = self.getmod(Con)
        self.intmod = self.getmod(Int)
        self.chamod = self.getmod(Cha)
        self.wismod = self.getmod(Wis)
        self.passperc = 10 + self.wismod
        self.lvl = self.getlvl(self.xp)
        self.profmod = self.getprofmod(self.lvl)
        self.proflist = proflist
        self.inv = []
        self.money = [0,0,0,0]
        self.loc = [0,0]

    def __repr__(self):
        return '{}'.format(self.name)

    def getmod(self, score):
        return floor((score - 10) / 2)

    def getlvl(self,xp):
        if xp >= 0:
            lvl = 1
        elif xp >= 300:
            lvl = 2
        elif xp >= 900:
            lvl = 3
        elif xp < 2700:
            lvl = 4
        elif xp >= 6500:
            lvl = 5
        elif xp >= 14000:
            lvl = 6
        elif xp >= 23000:
            lvl = 7
        elif xp >= 34000:
            lvl = 8
        elif xp >= 48000:
            lvl = 9
        elif xp >= 64000:
            lvl = 10
        elif xp >= 85000:
            lvl = 11
        elif xp >= 100000:
            lvl = 12
        elif xp >= 120000:
            lvl = 13
        elif xp >= 140000:
            lvl = 14
        elif xp >= 165000:
            lvl = 15
        elif xp >= 195000:
            lvl = 16
        elif xp >= 225000:
            lvl = 17
        elif xp >= 265000:
            lvl = 18
        elif xp >= 305000:
            lvl = 19
        elif xp >= 355000:
            lvl = 20
        return lvl

    def getprofmod(self,lvl):
        if lvl <= 4:
            profmod = 2
        elif lvl <= 8:
            profmod = 3
        elif lvl <= 12:
            profmod = 4
        elif lvl <= 16:
            profmod = 5
        else:
            profmod = 6
        return profmod

    def gainxp(self,newxp):
        player.xp = player.xp + newxp
        print("You have gained {} XP.".format(newxp))
        newlvl = self.getlvl(self,player.xp)
        if self.lvl != newlvl:
            self.lvl = newlvl
            sleep(1)
            print("You have leveled up to level {}!".format(newlvl))
            self.profmod = self.getprofmod(newlvl)
            print(self.profmod)

    def turn(self,field):
        if player not in combatants:
            return
        print("It is your turn to act. What will you do?")
        speed = player.speed
        actionturn = True
        moveturn = True
        while True:
            if player not in combatants:
                break
            command = input().lower()
            if command in ["o", "opt", "options"]:
                print(combatoptions)
                continue
            if command in ["m","move"] and moveturn == True:
                speed = speed - player.move(field,speed)
                print(speed)
                continue
            if command in ["a","atk","attack"]:
                if actionturn == True:
                    actionturn = False
                    player.attack(self.wep1,self.wep2)
                else:
                    print("You have already used your major action this turn.")
                    continue
            elif command in ["c","cst","cast"]:
                if actionturn == True:
                    actionturn = False
                    continue
                else:
                    print("You have already used your major action this turn.")
                    continue
            elif command in ["d","dash"]:
                if actionturn == True:
                    actionturn = False
                    speed = speed + player.speed
                    print("Your speed has been doubled.")
                    print(speed)
                    continue
                else:
                    print("You have already used your major action this turn.")
                    continue
            elif command in ["dis","disengage"]:
                if actionturn == True:
                    actionturn = False
                    continue
                else:
                    print("You have already used your major action this turn.")
                    continue
            elif command in ["dge","dodge"]:
                if actionturn == True:
                    actionturn = False
                    continue
                else:
                    print("You have already used your major action this turn.")
                    continue
            elif command in ["hlp","help"]:
                if actionturn == True:
                    actionturn = False
                    continue
                else:
                    print("You have already used your major action this turn.")
                    continue
            elif command in ["h","hide"]:
                if actionturn == True:
                    actionturn = False
                    continue
                else:
                    print("You have already used your major action this turn.")
                    continue
            elif command in ["r","ready"]:
                if actionturn == True:
                    actionturn = False
                    continue
                else:
                    print("You have already used your major action this turn.")
                    continue
            elif command in ["s","search"]:
                if actionturn == True:
                    actionturn = False
                    continue
                else:
                    print("You have already used your major action this turn.")
                    continue
            elif command in ["u","use"]:
                if actionturn == True:
                    actionturn = False
                    continue
                else:
                    print("You have already used your major action this turn.")
                    continue
            if command in ["e", "equip"]:
                print(player.wep1,player.wep2)
                self.equip()
                print(player.wep1,player.wep2)
                continue
            if command in ["end","end turn","turn end","finish","finished","finish turn",
                           "turn finished","done","turn done","turn over"]:
                return
            if actionturn == False and moveturn == False:
                if self.endturn() == True:
                    return
                else:
                    print("What will you do?")

    def gettarget(self,wep1,wep2):
        target = None
        while True:
            command = input().lower()
            if command in ["me","myself","yours truly"]:
                target = player
                break
            for combatant in combatants:
                if command == combatant.name.lower():
                    target = combatant
                    break
            else:
                for item in environment:
                    if command == item.name.lower():
                        target = item
                        break
            if target == None:
                continue
            else:
                break
        if checkadj(self.loc,target.loc) == False:
            dist = 5 * sqrt(((target.loc[0] - self.loc[0]) ** 2) + ((target.loc[0] - self.loc[1]) ** 2))
            dist = int(dist - (dist % 5))
        else:
            dist = 0
        return target,dist
    
    def attack(self,wep1,wep2):
        print("What is your target?")
        target,dist = self.gettarget(wep1,wep2)
        print(self.loc,target.loc,dist,wep1,wep1.shortrange,wep1.longrange,
              wep2,wep2.shortrange,wep2.longrange)
        if wep1.finesse == True and self.dexmod > self.strmod:
            atkmod = self.dexmod
        else:
            atkmod = self.strmod
        if wep1 in self.proflist:
            atkmod = atkmod + self.profmod
        if dist > wep1.shortrange:
            atkroll = disadvantage(1,20,atkmod + wep1.m)
            if dist > wep1.longrange:
                print("That target is out of range.")
                sleep(1)
                self.attack(wep1,wep2)
        else:
            atkroll = diceroll(1,20,atkmod + wep1.m)
        if atkroll - atkmod - wep1.m == 20:
            crit = True
        else:
            crit = False
        if atkroll >= target.ac or crit == True or target == player:
            print("The attack is successful.")
            sleep(1)
            if crit == True:
                print("Critical Hit!")
                sleep(1)
                dmgroll = diceroll(wep1.n * 2,wep1.d,wep1.m + atkmod)
            else:
                dmgroll = diceroll(wep1.n,wep1.d,wep1.m + atkmod)
            print("The " + target.name + " takes " + str(dmgroll) + " " + str(wep1.dmg) +
                  " damage.")
            sleep(1)
            target.hp = target.hp - dmgroll
        else:
            print("The attack misses.")
            sleep(1)
        if wep1.light == True and wep2.light == True:
            while True:
                print("What is your second target?")
                target,dist = self.gettarget(wep1,wep2)
                if wep2.finesse == True and self.dexmod > self.strmod:
                    atkmod = self.dexmod
                else:
                    atkmod = self.strmod
                if wep2 in self.proflist:
                    atkmod = atkmod + self.profmod
                if dist > wep1.shortrange:
                    atkroll = disadvantage(1,20,atkmod + wep1.m)
                    if dist > wep1.longrange:
                        print("That target is out of range.")
                        sleep(1)
                        continue
                atkroll = diceroll(1,20,atkmod + wep2.m)
                if atkroll - atkmod - wep2.m == 20:
                    crit = True
                if atkroll >= target.ac or crit == True:
                    print("The second attack is successful.")
                    sleep(1)
                    if crit == True:
                        dmgroll = diceroll(wep2.n * 2,wep2.d,wep2.m + atkmod)
                    else:
                        dmgroll = diceroll(wep2.n,wep2.d,wep2.m + atkmod)
                    print("The " + target.name + " takes " + str(dmgroll) + " " + str(wep2.dmg) +
                          " damage.")
                    sleep(1)
                    target.hp = target.hp - dmgroll
                else:
                    print("The second attack misses.")
                    sleep(1)
                break
        if target.hp <= 0:
            if target == player:
                print("The " + target.name + " has died.")
                sleep(1)
                target.alive = False
                combatants.remove(target)
                environment.append(target)

    def move(self,field,speed):
        print("To where are you moving?")
        while True:
            coord = input().lower()
            if len(coord) > 1:
                if coord[0] in ["(","[","{","<"] and coord[-1] in [")","]","}",">"]:
                    coord = coord[1:-1]
                coord = coord.split(",")
                if len(coord) == 2:
                    try:
                        xcoord = int(coord[0])
                        ycoord = int(coord[1])
                    except ValueError:
                        continue
                    try:
                       field[xcoord][ycoord] = player
                    except IndexError:
                        print("That coordinate is not in the field.")
                        continue
                    if [xcoord,ycoord] == player.loc:
                        print("You are already at that point.")
                        continue
                    dist = 5 * sqrt(((xcoord - player.loc[0]) ** 2) +
                                    ((ycoord - player.loc[1]) ** 2))
                    dist = int(dist - (dist % 5))
                    if dist > speed:
                        print("You cannot move that far.")
                        continue
                    break
        player.loc = [xcoord,ycoord]
        print("You have moved to " + str(xcoord) + "," + str(ycoord) + ".")
        return dist

    def equip(self):
        print("What weapon will you equip?")
        while True:
            command = input().lower()
            for item in player.inv:
                if command == item.name.lower():
                    if type(item) == weapon:
                        newwep = item
                    else:
                        newwep = weapon(item.name,item.desc,1,2,player.strmod,"bludgeoning",False,
                                        False,False,False,False,False,False,False,False,False)
                    break
            else:
                continue
            break
        player.wep1 = newwep
        print("You have equipped the {}.".format(item.name))
        if (newwep.light == True or newwep.versatile == True) and (player.wep2.light == True or
            player.wep2.versatile == True):
            player.wep2 = player.wep2
        else:
            player.wep2 = unarmed

    def endturn(self):
        print("Does that end your turn?")
        while True:
            command = input().lower()
            if checkyesno(command) == True:
                return True
            if checkyesno(command) == False:
                return False

class creature():
    def __init__(self,name,desc,size,ac,hp,maxhp,speed,strmod,dexmod,conmod,intmod,chamod,wismod,
                 passperc,alive):
        self.name = name
        self.desc = desc
        self.size = size
        self.ac = ac
        self.hp = hp
        self.maxhp = maxhp
        self.speed = speed
        self.strmod = strmod
        self.dexmod = dexmod
        self.conmod = conmod
        self.intmod = intmod
        self.chamod = chamod
        self.wismod = wismod
        self.passpperc = passperc
        self.loc = [0,0]

    def __repr__(self):
        return '{}'.format(self.name)

    def turn(self):
        print(self.name)

def createfield(l,w,combatants,environment):
    tile = 0
    field = [[tile for x in range(l)] for y in range(w)]
    for combatant in combatants:
        if combatant.loc == None:
            combatant.loc = [randint(0,l),randint(0,w)]
    for item in environment:
        if item.loc == None:
            item.loc = [randint(0,l),randint(0,w)]
    return(field)

def getinit(combatants):
    combatants.sort(key = lambda creature: diceroll(1,20,creature.dexmod), reverse = True)
    return combatants

def combat(combatants,environment,l,w):
    field = createfield(l,w,combatants,environment)
    print(field,field[0],field[0][0])
    combatants = getinit(combatants)
    while not(len(combatants) == 1 and combatants[0] == player):
        for combatant in combatants:
            if player not in combatants:
                break
            if combatant == player:
                player.turn(field)
            else:
                combatant.turn()
            if player not in combatants:
                break
        if player not in combatants:
            gameover()
    sleep(1)
    print()
    print("You have triumphed in combat!")
    sleep(1)
    newxp = 0
    for creature in killed:
        newxp = creature.cr + newxp
    gainxp(newxp)

stone = item("stone",0,3,"A small grey stone.",[2,3])
tree = item("tree",0,67,"A large redwood tree.",[1,4])
woodchest = item("wooden chest",50,5,"A simple empty wooden chest.",[1,1])

unarmed = weapon("hand",weapondesc["unarmed"],0,1,1,0,"bludgeoning",False,False,False,
                 True,False,[0,0],False,False,False,False)
dagger = weapon("dagger",weapondesc["dagger"],4,1,6,0,"piercing",False,False,False,True,False,0,
                False,False,False,False)
sword = weapon("sword",weapondesc["sword"],10,1,12,0,"slashing",False,False,False,True,False,0,
               False,False,False,10)
bow = weapon("bow",weapondesc["bow"],8,1,6,0,"piercing",True,False,False,False,False,[80,320],
             False,False,True,False)
superray = weapon("super ray","preposterously powerful weapon.",1000000,1,1,9999,"thunder",False,
                  False,False,False,False,[1000,5000],False,False,False,False)

player = player("Norman","human",3,"fighter",250,14,12,16,30,14,16,10,8,12,10,sword,dagger,
                [sword,dagger])

player.inv = [sword,bow,dagger,superray]
player.money = [200,12,45,90]

bat1 = creature("Bat 1",creaturedesc["bat"],2,12,diceroll(1,4,0),4,30,-4,2,-1,-4,-3,1,11,True)
bat2 = creature("Bat 2",creaturedesc["bat"],2,12,diceroll(1,4,0),4,30,-4,2,-1,-4,-3,1,11,True)
beholder = creature("Beholder",creaturedesc["beholder"],4,18,diceroll(19,10,76),266,20,0,2,4,3,3,2,
                    22,True)
reddragon = creature("Red Dragon",creaturedesc["reddragon"],5,19,diceroll(19,12,133),256,40,8,0,7,
                     3,5,1,23,False)

environment = [stone,tree,woodchest,reddragon]
combatants = [player,bat1,bat2,beholder]

beholder.loc = [10,5]
beholder.hp = 22
combat(combatants,environment,30,12)



#attack/fight/hit,cast,dash/run,move/walk,climb,swim,disengage,dodge,help,hide,ready,search/find,use,
#equip,unequip,wear/don,throw,drink,eat,doff,drop,grab/take/obtain,hit,kill,say/shout,
#go,feel/touch,give,play,read,cry,laugh,dance,describe,define,jump,rest/sleep,open,close/shut,
#look/examine,grapple
