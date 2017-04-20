from time import sleep
from random import randint
from random import choice
from math import floor

#definitions library

test = "test"
options = "[options_list_sample]"
laughter = "HAHAHAHAHA!"

racedesc = {"dark elf": "Dark Elves, also called Drow, are corrput and solitary Elves that " +
            "dwell in caves and deep undergound." +
            "\n +1 to Charisma, Superior Darkvision, Drow Magic",
            
            "dragonborn": "Dragonborn are a fearsome race of mages, scientists, and soldiers." +
            "\n +2 to Strength, +1 to Charisma, Breath Weapon, Dragonborn Resistance",

            "dwarf": "Dwarves are a hardy race of miners, smiths, and warriors. " +
            "\n +2 to Constitution, Darkvision, Dwarven Resilience",

            "elf": "Elves are a slender race of artists, nobles, and swordsmen." +
            "\n +2 to Dexterity, Darkvision, Keen Senses, Fey Ancestry",

            "forest gnome": "Forest Gnomes are an isolated type of Gnomes that tend to spend " +
            "their days in\n reclusive homes." +
            "\n +1 to Dexterity, Natural Illusionist",

            "gnome": "Gnomes are a curious race of tinkerers, outcasts, and pranksters." +
            "\n +2 to Intelligence, Darkvision, Gnome Cunning",

            "half elf": "Half Elves hold the blood of Humans and Elves, and can be found living " +
            "in either society." +
            "\n +2 to Dexterity, +1 to Intellignce, +1 to Charisma, Darkvision, Fey Ancestry",

            "high elf": "High Elves are a graceful and intelligent race of Elves that preside " +
            "in the upper class of society." +
            "\n +1 to Intelligence, Free Cantrip",

            "hill dwarf": "Hill Dwarves are the wise and prudent folk who live in plains and " +
            "lowlands." +
            "\n +1 to Wisdom, Dwarven Toughness",

            "half orc": "Half Orcs hold the blood of Humans and Orcs, and are often" +
            "considered as savage as their orcish fathers." +
            "\n +2 to Strength, +1 to Constitution, Darkvision, Relentless Endurance, " +
            "Savage Attack",

            "halfling": "Halflings are an cheerful race of musicians, bakers, and farmers." +
            "\n +2 to Dexterity, Lucky, Brave",

            "human": "Humans are a steadfast race that you already know about. Look in a mirror." +
            "\n +1 to All Ability Scores",

            "lightfoot halfling": "Lightfoot Halflings are a particularly small and affable " +
            "brand of Halflings." +
            "\n +1 to Charisma, Naturally Stealthy",

            "mountain dwarf": "Mountain Dwarves are especially robust fellows from living in " +
            "rugged terrain." +
            "\n +2 to Strength",

            "rock gnome": "Rock Gnomes are a friendlier, very inventive sort of Gnomes that " +
            "integrate themselves into bustling societies." +
            "\n +1 to Constitution, Tinkerer",

            "stout halfling": "Stout Halflings are Halflings that prefer to live in their own " +
            "small communities, called Shires." +
            "\n +1 to Constitution, Stout Resilience",

            "tiefling": "Tieflings are a people whose lineage derives from cursed Humans. They " +
            "are often despised and feared in society." +
            "\n +2 to Charisma, +1 to Intelligence, Darkvision, Hellish Resistance, " +
            "Infernal Legacy",

            "wood elf": "Wood Elves are calm and reserved Elves who hail from forests and " +
            "fenlands." +
            "\n +1 to Wisdom, Fleet of Foot, Mask of the Wild"}

classdesc = {"barbarian": "Barbarians are warriors who live and train in neverending battle, " +
             "and whose unbound rage fuels their ability to fight.",

             "bard": "Bards are magical performers who use their talents to cast spells and " +
             "inspire heroes.",

             "cleric": "Clerics are mages and healers who recieve the gift of divine magic as " +
             "adamant followers of a diety.",

             "druid": "Druids are mages whose primary goal is to protect the essence of nature. " +
             "Their magic ability comes from the innate power of the environment they serve.",

             "fighter": "Fighters are soldiers, mercenaries, and champions who have honed their " +
             "skills in battle into a method of decisive victory.",

             "monk": "Monks are members of a monastery or other order who seek enlightenment, " +
             "and control their chi as a way to master the self.",

             "paladin": "Paladins are religious knights who call forth the power of the gods " +
             "to bring justice, glory, or revenge upon the world.",

             "ranger": "Rangers are swift and steady hunters, archers, or tamers who attack " +
             "from afar.",

             "rogue": "Rogues are talented thieves, assassins, or tricksters who use the " +
             "elements of deceit and surprise to accomplish their goals.",

             "sorcerer": "Sorcerers are mages who have the innate ability to use magic due to " +
             "their unique bloodline.",

             "warlock": "Warlocks are mages who have received their abilities through some " +
             "mysterious deal or pact with a magical being from beyond the material planes.",

             "wizard": "Wizards are magical scholars who have studied and trained in the " +
             "practice of arcane magic."}

dragonbornnames = ["Arjhan","Balasar","Bharash","Donaar","Ghesh","Heskan","Kriv","Medrash","Mehen",
                   "Nadarr","Pandjed","Patrin","Rhogar","Shamash","Shedinn","Tarhun","Tiberius",
                   "Torinn","Akra","Biri","Daar","Farideh","Harann","Havijar","Jheri","Kava",
                   "Korinn","Mishann","Naj","Perra","Raiann","Sora","Surina","Thava","Uadjit"]

dwarfnames = ["Adrik","Alberich","Baern","Barendd","Brotto","Bruenor","Oain","Oarrak","Oelg",
              "Eberk","Einkil","Fargrim","Flint","Gardain","Harbek","Kildrak","Morgran","Orsik",
              "Oskar","Rangrim","Rurik","Taklinn","Thoradin","Thorin","Tordek","Traubon","Travok",
              "Ulfgar","Veit","Vondal","Amber","Artin","Audhild","Bardryn","Oagnal","Oiesa",
              "Eldeth","Falkrunn","Finellen","Gunnloda","Gurdis","Helja","Hlin","Kathra",
              "Kristryd","Lide","Liftrasa","Mardred","Riswynn","Sannl","Torbera","Torgga","Vist"]

elfnames = ["Ara","Bryn","Del","Eryn","Faen","Innil","Lael","Mella","Naill","Naeris","Phann",
            "Rael","Rinn","Sai","Syllin","Thia","Vali","Adran","Aelar","Aramil","Arannis","Aust",
            "Beiro","Berrian","Carrie","Enialis","Erdan","Erevan","Galinndan","Hadarai","Heian",
            "Himo","Immeral","Ivellios","Laucian","Mindartis","Paelias","Peren","Quarion",
            "Riardon","Rolen","Soveliss","Thamior","Tharivol","Theren","Varis","Adrie","Althaea",
            "Anastrianna","Andraste","Antinua","Bethrynna","Birel","Caelynn","Orusilia","Enna",
            "Felosial","Lelenia","Jelenneth","Keyleth","Leshanna","Lia","Meriele","Mialee",
            "Naivara","Quelenna","Quillathe","Sariel","Shanairra","Shava","Silaqui","Theirastra",
            "Thia","Vadania","Valanthe","Xanaphia"]

gnomenames = ["Alston","Alvyn","Boddynock","Brocc","Burgell","Dimble","Eldon","Erky","Fonkin",
              "Frug","Gerbo","Gimble","Glim","Jebeddo","Kellen","Namfoodle","Orryn","Quinlan",
              "Roondar","Scanlan","Seebo","Sindri","Warryn","Wrenn","Zook","Bimpnollin","Breena",
              "Caramip","Carlin","Donella","Duvamil","Ella","Ellyjobell","ElIywick,","Lilli",
              "Loopmottin","Lorilla","Mardnab","Nissa","Nyx","Oda","Orla","Pike","Roywyn","Shamil",
              "Tana","Waywocket","Zanna","Aleslosh","Ashhearth","Badger","Cloak","Doublelock",
              "Filchbatter","Fnipper","Ku","Nim","Oneshoe","Pock","Sparklegem","Stumbleduck"]

halforcnames = ["Deneh","Feng","Gell","Grog","Henk","Holg","Imsh","Kelh","Krusk","Mhurren","Ront",
                "Shump","Thokk","Baggi","Emen","Engong","Kansif","Myev","Neega","Ovak","Ownka",
                "Shaulha","Sulha","Vola","Volen","Yevelda"]

halflingnames = ["Alton","Ander","Cade","Corrin","Eldon","Errich","Finnan","Garret","Lindal",
                 "Lyle","Merric","Milo","Osborn","Perrin","Reed","Roscoe","Wellby","Andry","Bree",
                 "Callie","Cora","Euphemia","Jillian","Kithri","Lavinia","Lidda","Merla","Nedda",
                 "Paela","Portia","Seraphina","Shaena","Trym","Vani","Verna"]

humannames = ["Antonio","Arthur","Barry","Chad","Charles","Dave","Edward","Frederick","George",
              "Henry","Isaac","Jack","Jacob","Jason","Joren","Karl","Liam","Link","Macbeth",
              "Marcus","Matthew","Norman","Oliver","Percy","Ross","Samuel","Solaire","Stephen",
              "Wyatt","Xavier","Zachary","Amanda","Anne","Diane","Elizabeth","Gwendalyn","Jane",
              "Karen","Katherine","Laura","Lucy","Nataly","Nora","Pauline","Penelope","Sophia",
              "Victoria","Violet","Wendy"]

tieflingnames = ["Akmenos","Amnon","Barakas","Damakos","Ekemon","Iados","Kairon","Leucis","Melech",
                 "Mordai","Morthos","Pelaios","Skamos","Therai","Akta","Anakis","Bryseis",
                 "Criella","Damaia","Ea","Kallista","Lerissa","Makaria","Nemeia","Orianna",
                 "Phelaia","Rieta","Art","Carrion","Chant","Creed","Despair","Excellence","Fear",
                 "Glory","Hope","Ideal","Music","Nowhere","Open","Poetry","Quest","Random",
                 "Reverence","Sorrow","Temerily","Torment","Weary"]

#commands library

def diceroll(n,d,m):
    x = 0
    for roll in range(0,n):
        x = x + randint(1,d)
    x = x + m
    return x

def buffer():
    for buffer in range(0,5):
        print(".")
        sleep(0.5)

def checkyesno(command):
    if command in ["y","ye","ya","yes","yup","yeah","yea","ok","okay","sure","aye","indeed",
                   "affirmative","si","ja"]:
        return True
    elif command in ["n","no","nope","nah","nay","negative","negatory","nein"]:
        return False
    else:
        return
   
def checkcommand(command):
    if command in ["o","opt","option","options"]:
        print(options)
    if command in ["laugh","laughter","ha","hah","haha"]:
        print(laughter)
    else:
        return False

#title screen

print("WELCOME TO POTIONS & PYTHONS!")
print("Type \"options\" at any time for a list of commands.")
print("Type \"play\" to begin your adventure.")

def startgame():
    command = input().lower()
    if checkcommand(command):
        startgame()
    elif command == "play":
        return
    else: startgame()

#character creation

def subracemenu(race):
    if race == "dwarf":
        sleep(1)
        command = input("Are you a Hill Dwarf or a Mountain Dwarf?\n").lower()
        sleep(1)
        if command in ["hill dwarf","hill"]:
            return "Hill Dwarf"
        elif command in ["mountain dwarf","mountain"]:
            return "Mountain Dwarf"
        else:
            return subracemenu(race)
    if race == "elf":
        sleep(1)
        command = input("Are you a High Elf, a Wood Elf, or a Dark Elf?\n").lower()
        sleep(1)
        if command in ["high elf","high"]:
            return "High Elf"
        elif command in ["wood elf","wood"]:
            return "Wood Elf"
        elif command in ["dark elf","dark"]:
            return "Dark Elf"
        else:
            return subracemenu(race)
    if race == "gnome":
        sleep(1)
        command = input("Are you a Forest Gnome or a Rock Gnome?\n").lower()
        sleep(1)
        if command in ["forest gnome","forest"]:
            return "Forest Gnome"
        elif command in ["rock gnome","rock"]:
            return "Rock Gnome"
        else:
            return subracemenu(race)
    if race == "halfling":
        sleep(1)
        command = input("Are you a Lightfoot Halfling or a Stout Halfling?\n").lower()
        sleep(1)
        if command in ["lightfoot halfling","lightfoot"]:
            return "Lightfoot Halfling"
        elif command in ["stout halfling","stout"]:
            return "Stout Halfling"
        else:
            return subracemenu(race)

def racemenu():
        command = input().lower()
        sleep(1)
        if checkcommand(command) is True:
            return racemenu()
        elif command == "random":
            return "random"
        elif command in ["describe dragonborn","describe dragonborns"]:
            print(racedesc["dragonborn"])
            return racemenu()
        elif command in ["describe dwarf","describe dwarfs","describe dwarves"]:
            print(racedesc["dwarf"])
            return racemenu()
        elif command in ["describe elf","describe elfs","describe elves"]:
            print(racedesc["elf"])
            return racemenu()
        elif command in ["describe gnome","describe gnomes"]:
            print(racedesc["gnome"])
            return racemenu()
        elif command in ["describe half elf","describe half elfs","describe half elves"]:
            print(racedesc["half elf"])
            return racemenu()
        elif command in ["describe half orc","describe half orcs"]:
            print(racedesc["half orc"])
            return racemenu()
        elif command in ["describe halfling","describe halflings"]:
            print(racedesc["halfling"])
            return racemenu()
        elif command in ["describe human","describe humans"]:
            print(racedesc["human"])
            return racemenu()
        elif command in ["describe tiefling","describe tieflings"]:
            print(racedesc["tiefling"])
            return racemenu()
        elif command == "dragonborn":
            return "Dragonborn"
        elif command == "dwarf":
            sleep(1)
            print(racedesc["hill dwarf"])
            sleep(1)
            print(racedesc["mountain dwarf"])
            return subracemenu("dwarf")
        elif command == "elf":
            sleep(1)
            print(racedesc["high elf"])
            sleep(1)
            print(racedesc["wood elf"])
            sleep(1)
            print(racedesc["dark elf"])
            return subracemenu("elf")
        elif command == "gnome":
            sleep(1)
            print(racedesc["forest gnome"])
            sleep(1)
            print(racedesc["rock gnome"])
            return subracemenu("gnome")
        elif command == "half elf":
            return "Half Elf"
        elif command == "half orc":
            return "Half Orc"
        elif command == "halfling":
            sleep(1)
            print(racedesc["lightfoot halfling"])
            sleep(1)
            print(racedesc["stout halfling"])
            return subracemenu("halfling")
        elif command == "human":
            return "Human"
        elif command == "tiefling":
            return "Tiefling"
        else:
            return racemenu()
        
def classmenu():
        command = input().lower()
        sleep(1)
        if checkcommand(command) is True:
            return classmenu()
        elif command in ["describe barbarian","describe barbarians"]:
            print(classdesc["barbarian"])
            return classmenu()
        elif command in ["describe bard","describe bards"]:
            print(classdesc["bard"])
            return classmenu()
        elif command in ["describe cleric","describe clerics"]:
            print(classdesc["cleric"])
            return classmenu()
        elif command in ["describe druid","describe druids"]:
            print(classdesc["druid"])
            return classmenu()
        elif command in ["describe fighter","describe fighters"]:
            print(classdesc["fighter"])
            return classmenu()
        elif command in ["describe monk","describe monks"]:
            print(classdesc["monk"])
            return classmenu()
        elif command in ["describe paladin","describe paladins"]:
            print(classdesc["paladin"])
            return classmenu()
        elif command in ["describe ranger","describe rangers"]:
            print(classdesc["ranger"])
            return classmenu()
        elif command in ["describe rogue","describe rogues"]:
            print(classdesc["rogue"])
            return classmenu()
        elif command in ["describe sorcerer","decribe sorcerers"]:
            print(classdesc["sorcerer"])
            return classmenu()
        elif command in ["describe warlock","describe warlocks"]:
            print(classdesc["warlock"])
            return classmenu()
        elif command in ["describe wizard","describe wizards"]:
            print(classdesc["wizard"])
            return classmenu()
        elif command == "barbarian":
            return "Barbarian"
        elif command == "bard":
            return "Bard"
        elif command == "cleric":
            return "Cleric"
        elif command == "druid":
            return "Druid"
        elif command == "fighter":
            return "Fighter"
        elif command == "monk":
            return "Monk"
        elif command == "paladin":
            return "Paladin"
        elif command == "ranger":
            return "Ranger"
        elif command == "rogue":
            return "Rogue"
        elif command == "sorcerer":
            return "Sorcerer"
        elif command == "warlock":
            return "Warlock"
        elif command == "wizard":
            return "Wizard"
        else:
            return classmenu()

def getabilityscores():
        score1 = 0
        score2 = 0
        score3 = 0
        score4 = 0
        score5 = 0
        score6 = 0
        scorelist = [score1,score2,score3,score4,score5,score6]
        for score in range(0,len(scorelist)):
            a = randint(1,6)
            b = randint(1,6)
            c = randint(1,6)
            d = randint(1,6)
            scorelist[score] = a + b + c + d - min(a,b,c,d)
        scorelist = sorted(scorelist)
        return(scorelist)

def scoremenu(ability,score,scorelist):
        print("Choose your " + str(ability) + " score.")
        sleep(1)
        print(scorelist)
        try:
            command = int(input().lower())
            sleep(1)
            if command == scorelist[0]:
                score = scorelist[0]
                del scorelist[0]
            elif command == scorelist[1]:
                score = scorelist[1]
                del scorelist[1]
            elif command == scorelist[2]:
                score = scorelist[2]
                del scorelist[2]
            elif command == scorelist[3]:
                score = scorelist[3]
                del scorelist[3]
            elif command == scorelist[4]:
                score = scorelist[4]
                del scorelist[4]
            elif command == scorelist[5]:
                score = scorelist[5]
                del scorelist[5]
            else:
                print("That is not one of your ability scores.")
                sleep(1)
                return scoremenu(ability,score,scorelist)
            print("Your " + ability + " score is " + str(score) + ".")
            return score
        except:
            print("That is not one of your ability scores.")
            sleep(1)
            return scoremenu(ability,score,scorelist)

def randomscore(scorelist,score1,score2,score3,score4,score5,score6):
        score1 = scorelist[5]
        score2 = scorelist[4]
        x = choice(scorelist[:3])
        score3 = x
        del x
        x = choice(scorelist[:3])
        score4 = x
        del x
        x = choice(scorelist[:3])
        score5 = x
        del x
        x = choice(scorelist[:3])
        score6 = x
        del x
        return (score1,score2,score3,score4,score5,score6)

def randomcharacter():
    characterrace = choice(["Dark Elf","Dragonborn","Forest Gnome","Half Elf","Half Orc",
                             "High Elf","Hill Dwarf","Human","Lightfoot Halfling","Mountain Dwarf",
                             "Rock Gnome","Stout Halfling","Tiefling","Wood Elf"])
    characterclass = choice(["Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin",
                              "Ranger","Rogue","Sorcerer","Warlock","Wizard"])
    
    STR = None
    DEX = None
    CON = None
    INT = None
    CHA = None
    WIS = None

    scorelist = getabilityscores()
    
    if characterclass == "Barbarian":
        STR,CON,DEX,INT,WIS,CHA = randomscore(scorelist,STR,CON,DEX,INT,WIS,CHA)
    if characterclass == "Bard":
        CHA,DEX,STR,CON,INT,WIS = randomscore(scorelist,CHA,DEX,STR,CON,INT,WIS)
    if characterclass == "Cleric":
        WIS,CON,CHA,DEX,STR,INT = randomscore(scorelist,WIS,CON,CHA,DEX,STR,INT)
    if characterclass == "Druid":
        WIS,DEX,CHA,CON,STR,INT = randomscore(scorelist,WIS,DEX,CHA,CON,STR,INT)
    if characterclass == "Fighter":
        STR,DEX,CHA,CON,WIS,INT = randomscore(scorelist,STR,DEX,CHA,CON,WIS,INT)
    if characterclass == "Monk":
        DEX,WIS,CHA,CON,STR,INT = randomscore(scorelist,DEX,WIS,CHA,CON,STR,INT)
    if characterclass == "Paladin":
        STR,CHA,DEX,CON,WIS,INT = randomscore(scorelist,STR,CHA,DEX,CON,WIS,INT)
    if characterclass == "Ranger":
        DEX,WIS,CHA,CON,STR,INT = randomscore(scorelist,DEX,WIS,CHA,CON,STR,INT)
    if characterclass == "Rogue":
        DEX,INT,STR,CON,WIS,CHA = randomscore(scorelist,DEX,INT,STR,CON,WIS,CHA)
    if characterclass == "Sorcerer":
        CHA,DEX,STR,CON,WIS,INT = randomscore(scorelist,CHA,DEX,STR,CON,WIS,INT)
    if characterclass == "Warlock":
        CHA,CON,STR,DEX,WIS,INT = randomscore(scorelist,CHA,CON,STR,DEX,WIS,INT)
    if characterclass == "Wizard":
        INT,DEX,CHA,CON,WIS,STR = randomscore(scorelist,INT,DEX,CHA,CON,WIS,STR)

    if characterrace == "Dark Elf":
        charactername = choice(elfnames)
    if characterrace == "Dragonborn":
        charactername = choice(dragonbornnames)
    if characterrace == "Forest Gnome":
        charactername = choice(gnomenames)
    if characterrace == "Half Elf":
        charactername = choice(elfnames + humannames)
    if characterrace == "Half Orc":
        charactername = choice(halforcnames + humannames)
    if characterrace == "High Elf":
        charactername = choice(elfnames)
    if characterrace == "Hill Dwarf":
        charactername = choice(dwarfnames)
    if characterrace == "Human":
        charactername = choice(humannames)
    if characterrace == "Lightfoot Halfling":
        charactername = choice(halflingnames)
    if characterrace == "Mountain Dwarf":
        charactername = choice(dwarfnames)
    if characterrace == "Rock Gnome":
        charactername = choice(gnomenames)
    if characterrace == "Stout Halfling":
        charactername = choice(halflingnames)
    if characterrace == "Tiefling":
        charactername = choice(tieflingnames)
    if characterrace == "Wood Elf":
    	charactername = choice(elfnames)

    return(characterrace,characterclass,STR,DEX,CON,INT,CHA,WIS,charactername)

def characterrestart():
        sleep(1)
        print("Is this character okay?")
        command = input().lower()
        sleep(1)
        if checkyesno(command) is True:
            print()
        elif checkyesno(command) is False:
            print("Would you like to make a new character?")
            command = input().lower()
            if checkyesno(command) is True:
                sleep(1)
                buffer()
                return True
            elif checkyesno(command) is False:
                sleep(1)
                print("You must decide.")
                return characterrestart()
            else:
                return characterrestart() 
        else:
            return characterrestart()

def charactercreation():
    characterrace = None
    characterclass = None
    STR = None
    DEX = None
    CON = None
    INT = None
    WIS = None
    CHA = None
    charactername = None

    #race selection

    sleep(0.5)
    print("Choose your race.")
    print()
    sleep(1)
    print("Dragonborn")
    print("Dwarf")
    print("Elf")
    print("Gnome")
    print("Half Elf")
    print("Half Orc")
    print("Halfling")
    print("Human")
    print("Tiefling")
    print()
    sleep(1)
    print("Type \"describe <race>\" to learn more about any of these races.")
    sleep(1)
    print("Type \"random\" to randomly generate a character.")

    characterrace = racemenu()

    if characterrace == "random":
        characterrace,characterclass,STR,DEX,CON,INT,CHA,WIS,charactername = randomcharacter()
    else: 
        print("You are a " + characterrace + ".")

        sleep(1)
        buffer()

        #class selection

        sleep(0.5)
        print("Choose your class.")
        print()
        sleep(1)
        print("Barbarian")
        print("Bard")
        print("Cleric")
        print("Druid")
        print("Fighter")
        print("Monk")
        print("Paladin")
        print("Ranger")
        print("Rogue")
        print("Sorcerer")
        print("Warlock")
        print("Wizard")
        print()
        sleep(1)
        print("Type \"describe <class>\" to learn more about any of these classes.")

        characterclass = classmenu()

        print("You are a " + characterclass + ".")

        sleep(1)
        buffer()

        #ability scores

        scorelist = getabilityscores()

        sleep(0.5)
        print("Your ability scores will now be determined.")
        sleep(3)
        print(scorelist)
        sleep(3)
        print("These are your six ability scores. Attribute one of these numbers to each " +\
              "of your\n abilities.")
        sleep(3)
        print()

        print("Strength is your athletic prowess and raw physical power.")
        sleep(1)
        STR = scoremenu("strength",STR,scorelist)
        sleep(1)
        print()
            
        print("Dexterity is your agility and manual skill.")
        sleep(1)
        DEX = scoremenu("dexterity",DEX,scorelist)
        sleep(1)
        print()
            
        print("Constitution is your physical endurance and vitality.")
        sleep(1)
        CON = scoremenu("constitution",CON,scorelist)
        sleep(1)
        print()
            
        print("Intelligence is your amassed knowledge and affinity for strategic thought.")
        sleep(1)
        INT = scoremenu("intelligence",INT,scorelist)
        sleep(1)
        print()
            
        print("Charisma is your charm and force of will.")
        sleep(1)
        CHA = scoremenu("charisma",CHA,scorelist)
        sleep(1)
        print()
            
        print("Wisdom is your innate ability to sense and reason.")
        sleep(1)
        WIS = scorelist[0]
        del scorelist[0]
        print("Your Wisdom score is " + str(WIS) + ".")

        sleep(1)
        buffer()
        
        #character name
        
        sleep(0.5)
        print("And finally, choose your name.")
        charactername = input()

        sleep(1)
        buffer()

    #racial bonuses

    if characterrace == "Dark Elf":
        DEX = DEX + 2
        CHA = CHA + 1
    if characterrace == "Dragonborn":
        STR = STR + 2
        CHA = CHA + 1
    if characterrace == "Forest Gnome":
        INT = INT + 2
        DEX = DEX + 1
    if characterrace == "Half Elf":
        DEX = DEX + 2
        INT = INT + 1
        CHA = CHA + 1
    if characterrace == "Half Orc":
        STR = STR + 2
        CON = CON + 1
    if characterrace == "High Elf":
        DEX = DEX + 2
        INT = INT + 1
    if characterrace == "Hill Dwarf":
        CON = CON + 2
        WIS = WIS + 1
    if characterrace == "Human":
        STR = STR + 1
        DEX = DEX + 1
        CON = CON + 1
        INT = INT + 1
        CHA = CHA + 1
        WIS = WIS + 1
    if characterrace == "Lightfoot Halfling":
        DEX = DEX + 2
        CHA = CHA + 1
    if characterrace == "Mountain Dwarf":
        CON = CON + 2
        STR = STR + 1
    if characterrace == "Rock Gnome":
        INT = INT + 2
        CON = CON + 1
    if characterrace == "Stout Halfling":
        DEX = DEX + 2
        CON = CON + 1
    if characterrace == "Tiefling":
        CHA = CHA + 2
        INT = INT + 1
        
    #confirm character creation

    sleep(2)
    print("You are \"" + charactername + "\" the " + characterrace + " " + characterclass + ".")
    print("Str: " + str(STR) + ", Dex: " + str(DEX) + ", Con: " + str(CON) + ", Int: " + str(INT) +
          ", Cha: " + str(CHA) + ", Wis: " + str(WIS))
    
    if characterrestart():
        return charactercreation()
    else:
        return (characterrace,characterclass,STR,DEX,CON,INT,CHA,WIS,charactername)

startgame()

buffer()
   
characterrace,characterclass,STR,DEX,CON,INT,CHA,WIS,charactername = charactercreation()



#end of code

sleep(0.5)
print()
sleep(0.5)
print("[end_of_code]")
