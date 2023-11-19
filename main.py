#Adventure Game John_Moreau
import random
import time

#Sources:
# https://stackoverflow.com/questions/60608275/how-can-i-print-text-so-it-looks-like-its-being-typed-out
# https://www.asciiart.eu/mythology/dragons

#TODO IDEAS:
# Add more loot
# Add more enemies
# Add riddle event
# Add spells
# Add classes
# Add hints to what is in each tunnel sometimes
# Add Binary Tree to generate tunnels and enemies/loot


# Declare Global Variables
debug = False
exit = False
gameOver = False
textSpeed = "slow"


# Define a function to print output slowly
def printSlowly(text):
    if debug:
        print(text)
        return
    lastChar = ""
    for char in text:
        print(char, end='')
        if char == "." and lastChar != ".":
            time.sleep(0.3)
        else:
            if textSpeed == "slow":
                time.sleep(random.choice([
                    0.07, 0.05, 0.04, 0.04, 0.03, 0.03, 0.03, 0.02
                    ]))
            else:
                time.sleep(random.choice([
                0.03, 0.02, 0.02, 0.02, 0.03, 0.01, 0.01, 0
                ]))
        lastChar = char
    print()
        
# Define a function to roll a D20
def rollD20(threshold, bonus) -> bool:
    input(f"Press Enter to roll a D20. You must roll a {str(threshold)} or higher. ") # Example of inline variables using f strings
    roll = random.randint(1,20)
    printSlowly(f"You roll {str(roll)} + {str(bonus)} bonus from your equipment.")
    input("Press Enter to continue.")
    if roll + bonus >= threshold:
        return True
    else:
        return False

def rollEscape() -> bool:
    if random.randint(1,3) > 1:
        return True
    else:
        return False

def rollLoot() -> bool:
    lootRollThreshold = random.randint(5,10)
    return rollD20(lootRollThreshold, getPlayerRollBonus("loot"))
     

def getPlayerRollBonus(type) -> int:
    playerRollBonus = 0
    
    if type == "combat":
        if playerWeapons:
            playerRollBonus += 6
        if dragonScaleFound:
            playerRollBonus += 3
        if sapphireAmuletFound:
            playerRollBonus += 1
        if boneToothFound:
            playerRollBonus += 2
    else:
        if dragonScaleFound:
            playerRollBonus += 2
        if sapphireAmuletFound:
            playerRollBonus += 5
        if boneToothFound:
            playerRollBonus += 1

    return playerRollBonus

   

# Main Game Loop
while not exit:
    gameOver = False
    # Main Menu
    print(r"                 ___====-_  _-====___")
    print(r"           _--^^^#####//      \\\\#####^^^--_")
    print(r"        _-^##########// (    ) \\\\##########^-_")
    print(r"       -############//  |\^^/|  \\############-")
    print(r"     _/############//   (@::@)   \\############\_")
    print(r"    /#############((     \\//     ))#############\-")
    print(r"   -###############\\    (oo)    //###############-")
    print(r"  -#################\\  / VV \  //#################-")
    print(r" -###################\\/      \//###################-")
    print(r"_#/|##########/\######(   /\   )######/\##########|\#_")
    print(r"|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|")
    print(r"`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '")
    print(r"   `   `  `      `   / | |  | | \   '      '  '   '")
    print(r"                    (  | |  | |  )")
    print(r"                   __\ | |  | | /__")
    print(r"                  (vvv(VVV)(VVV)vvv)")
    print(r"")
    printSlowly("          Welcome to the Adventure Game!")
    printSlowly("        CSS115 | 11-17-23 | by John Moreau")
    print("                 1. Start Game")
    print(f"                 2. Change Text Speed (Current: {textSpeed})")
    print("                 3. Exit")
    menuChoice = 0
    while menuChoice > 3 or menuChoice < 1:
        try:
            menuChoice = int(input("What would you like to do? (1, 2 or 3) "))
        except:
            continue
    if menuChoice == 2:
        if textSpeed == "slow":
            textSpeed = "fast"
        else:
            textSpeed = "slow"
        printSlowly(f"Text speed set to {textSpeed}.")
        continue
    if menuChoice == 3:
        exit = True
        break
    
    
    # Start Game
    printSlowly("You wake up on the cold stone floor of a cave.")
    printSlowly("It's dark and quiet. The walls and floor around you are damp and covered in moss and slime.")
    printSlowly("You sit up and feel around in the darkness for your torch and equipment.")
    printSlowly("You find your torch and light it with a minor sparking spell. You are in a small room with two tunnels in front of you.")
    while not gameOver:
        printSlowly ("You appear to be lost in an underground cave. You must find your way out.")
        printSlowly("..............")
        # New Game
        dragonThreshold = random.randint(14,16)
        trollThreshold = random.randint(7,10)
        goblinThreshold = random.randint(3,6)
        trappedChestThreshold = random.randint(3,7)
        TunnelExit = random.randint(8,14)
        # lootRollThreshold = 
        # Player Variables
        playerWeapons = False
        secretTunnelFound = False
        dragonDefeated = False
        trollDefeated = False
        goblinDefeated = False
        dragonScaleFound = False
        sapphireAmuletFound = False
        boneToothFound = False
        playerLootRollBonus = 0
        playerCombatRollBonus = 0
        lastPlayerTunnelCount = 0
        playerTunnelCount = 0
        playerLoot = []
        playerGoldCount = 0
        goblinSlayCount = 0
        
        
        # While the player has not found the exit
        while playerTunnelCount < TunnelExit:
            
            if gameOver:
                break
            
            
            if playerTunnelCount == lastPlayerTunnelCount and playerTunnelCount > 0:
                printSlowly("The two tunnels look different from before...")

            dragonTunnel = random.randint(1,16)
            trollTunnel = random.randint(1,9)
            goblinTunnel = random.randint(1,6)
            lootTunnel = random.randint(1,5)
            secretTunnel = random.randint(1,4)
            
            
            tunnelChoice = 0
            # Get tunnel choice
            while tunnelChoice > 2 or tunnelChoice < 1:
                try:
                    tunnelChoice = int(input("There are two tunnels in front of you, which one do you take? (1 or 2): "))
                except:
                    continue
            
            # Check result of tunnel choice
            
            # Secret Tunnel
            if tunnelChoice == secretTunnel and secretTunnelFound == False:
                printSlowly("You lean against the wall to rest for just a moment. Suddenly you hear a loud click and the wall opens up to a secret tunnel!")
                printSlowly("In front of you is a large wooden chest illuminated by moonlight from a crack in the cave ceiling above.")
                chestChoice = 0
                while chestChoice > 2 or chestChoice < 1:
                    try:
                        chestChoice = int(input("Do you open the chest? (1) Yes, (2) No "))
                    except:
                        continue
                if chestChoice == 1:
                    if rollD20(trappedChestThreshold, getPlayerRollBonus("loot")):
                        printSlowly("You open the chest. Inside is a thick layer of black soot and dust. You find a steel sword with a ruby embeded in the hilt, and metal shield with a fire emblem. You equip them and head back the way you came.")
                        playerWeapons = True
                        secretTunnelFound = True # To prevent the player from finding the chest again
                        playerLoot.append("Ruby Steel Sword")
                        playerLoot.append("Metal Fire Shield")
                    else:
                        chestContents = random.randint(1,3)
                        if chestContents == 1:
                            printSlowly("You open the chest, somewhere you hear a stone move. A dart shoots out of the darkness and hits you in the back. You fall over and the world starts to fade.")
                            break
                        elif chestContents == 2:
                            printSlowly("You open the chest. Inside is a thick layer of black soot and dust. You find a small pouch of 10 gold pieces. You put it in your pocket and head back the way you came.")
                            playerGoldCount += 10
                        else:
                            printSlowly("You open the chest. Inside is a thick layer of black soot and dust. You find nothing of value. You head back the way you came.")
                else:
                    printSlowly ("You leave the chest alone and go back the way you came.")
                playerTunnelCount -= 1 # Go back one tunnel
                
            # Dragon Tunnel
            elif tunnelChoice == dragonTunnel and dragonDefeated == False:
                printSlowly ("You enter the tunnel. Suddenly you hear a low rumbling growl and see a pair of huge glowing eyes in the darkness. You've entered the tunnel with a dragon!")
                print("                                             __----~~~~~~~~~~~------___")
                print("                                  .  .   ~~//====......          __--~ ~~")
                print("                  -.            \\_|//     |||\\\\  ~~~~~~::::... /~")
                print("               ___-==_       _-~o~  \\/    |||  \\\\            _/~~-")
                print("       __---~~~.==~||\\=_    -_--~/_-~|-   |\\\\   \\\\        _/~")
                print("   _-~~     .=~    |  \\\\-_    '-~7  /-   /  ||    \\      /")
                print(" .~       .~       |   \\\\ -_    /  /-   /   ||      \\   /")
                print("/  ____  /         |     \\\\ ~-_/  /|- _/   .||       \\ /")
                print("|~~    ~~|--~~~~--_ \\     ~==-/   | \\~--===~~        .\\")
                print("         '         ~-|      /|    |-~\\~~       __--~~")
                print("                     |-~~-_/ |    |   ~\\_   _-~            /\\")
                print("                          /  \\     \\__   \\/~                \\__")
                print("                      _--~ _/ | .-~~____--~-/                  ~~==.")
                print("                     ((->/~   '.|||' -_|    ~~-/ ,              . _|")
                print("                                -_     ~\\      ~~---l__i__i__i--~~_/")
                print("                                _-~-__   ~)  \\--______________--~~")
                print("                              //.-~~~-~_--~- |-------~~~~~~~~")
                #Roll a D20 to see if the player can defeat the dragon or escape
                if not rollD20(dragonThreshold, getPlayerRollBonus("combat")):
                    if not rollEscape():
                        printSlowly ("The dragon leaps out of the darkness and swallows you whole. The world starts to fade.")
                        gameOver = True
                        continue
                    else:
                        printSlowly("The dragon lets out a loud roar and unleashes a jet of fire at you. You roll out of the way and the flames hit the wall behind you. You run back the way you came.")
                        printSlowly ("You narrowly escape the dragon.")
                        playerTunnelCount -= 1 # Go back one tunnel
                elif playerWeapons:
                    printSlowly("The dragon lets out a loud roar and unleashes a jet of fire at you. You raise your shield and deflect the flames. You charge at the dragon and stab it in the chest.")
                    printSlowly("The dragon lets out a loud roar and falls to the ground in a large plume of dust and smoke.")
                    printSlowly ("You defeat the dragon.")
                    dragonDefeated = True
                    printSlowly("You look around the area for loot...")
                    if rollLoot():
                        printSlowly("You find the dragon's hoard of gold it was guarding... there's too much to carry, but you manage to stuff 200 gold pieces into your pockets.")
                        playerGoldCount += 200
                        printSlowly("You also find a small red shimmering pearlescent scale on the floor. You feel the heat as you pick it up, it warms your hands and fills you with a strong sense of fighting spirit. You put it in your side pouch.")
                        dragonScaleFound = True
                        playerLoot.append("Dragon Scale")
                    else:
                        printSlowly("You find nothing of value.")
                else:
                    printSlowly("The dragon lets out a loud roar and unleashes a jet of fire at you. You roll out of the way and the flames hit the wall behind you. You run back the way you came.")
                    printSlowly ("You escape the dragon.")
                    playerTunnelCount -= 1 # Go back one tunnel
            
            # Troll Tunnel   
            elif tunnelChoice == trollTunnel and trollDefeated == False:
                printSlowly ("You enter the tunnel. Suddenly you hear a low rumbling slow growl. A large creature towers over you. You've entered the tunnel with a troll!")
                #Roll a D20 to see if the player can defeat the troll or escape
                if not rollD20(trollThreshold, getPlayerRollBonus("combat")):
                    if not rollEscape():
                        printSlowly ("The troll leaps out of the darkness and smashes you with a wooden club. The world starts to fade.")
                        gameOver = True
                        continue
                    else:
                        printSlowly("The troll lets out a loud roar and charges at you. You roll out of the way and the troll hits the wall behind you, dazed. You run back the way you came.")
                        printSlowly ("You escape the troll.")
                        playerTunnelCount -= 1 # Go back one tunnel
                elif playerWeapons:
                    printSlowly("The troll lets out a loud roar and charges at you. You raise your shield and sword to fight. You roll to dodge the trolls attack and stab it in the ribs.")
                    printSlowly("The troll lets out a deep wail and falls to the ground with a thud.")
                    printSlowly ("You defeat the troll.")
                    trollDefeated = True
                    printSlowly("You look around the area for loot...")
                    if rollLoot():
                        goldRoll = random.randint(5,25)
                        printSlowly(f"You find a small pouch of {goldRoll} gold on the troll's body.")
                        playerGoldCount += goldRoll
                        printSlowly("You also find a small amulet made of petrified dark wood with Sapphires embeded around the edges. You put it around your neck for good luck.")
                        sapphireAmuletFound = True
                        playerLoot.append("Sapphire Amulet")
                    else:
                        printSlowly("You find nothing of value.")
                else:
                    printSlowly("The troll lets out a loud roar and charges at you. You roll out of the way and the troll hits the wall behind you, dazed. You run back the way you came.")
                    printSlowly ("You escape the troll.")
                    playerTunnelCount -= 1 # Go back one tunnel
                    
            # Goblin Tunnel
            elif tunnelChoice == goblinTunnel:
                printSlowly ("You enter the tunnel. Suddenly you hear a loud growl and see a pair of glowing eyes in the darkness. You've entered the tunnel with a goblin!")
                #Roll a D20 to see if the player can defeat the goblin or escape
                if not rollD20(goblinThreshold, getPlayerRollBonus("combat")):
                    if not rollEscape():
                        printSlowly ("The goblin leaps out of the darkness and stabs you with a rusty dagger. The world starts to fade.")
                        gameOver = True
                        continue
                    else:
                        printSlowly("The goblin lets out a loud screetch and charges at you. You roll out of the way and the goblin stabs the empty air where you stood just moments before. You run back the way you came.")
                        printSlowly ("You narrowly escape the goblin.")
                        playerTunnelCount -= 1
                elif playerWeapons:
                    printSlowly("The goblin lets out a loud roar and charges at you. You raise your shield and sword to fight. You roll to dodge the goblin's wild attack and swiftly cut off it's head.")
                    printSlowly("The goblin falls to the ground and it's head rolls away.")
                    printSlowly ("You defeat the goblin.")
                    goblinDefeated = True
                    goblinSlayCount += 1
                    printSlowly("You look around the area for loot...")
                    if rollLoot():
                        goldRoll = random.randint(5,15)
                        printSlowly(f"You find a small pouch of {str(goldRoll)} gold on the goblin's body.")
                        playerGoldCount += goldRoll
                        if not boneToothFound:
                            printSlowly("You also find a large bone tooth on a leather strap around the goblin's wrist. You remove the charm and place it on your arm for good luck. Maybe this will scare off other goblins?")
                            boneToothFound = True
                            playerLoot.append("Bone Tooth")
                    else:
                        printSlowly("You find nothing of value.")
                else:
                    printSlowly("The goblin lets out a loud screetch and charges at you. You roll out of the way and the goblin stabs the empty air where you stood just moments before. You run back the way you came.")
                    printSlowly ("You escape the goblin.")
                    playerTunnelCount -= 1 # Go back one tunnel
                            
            # Loot Tunnel
            elif tunnelChoice == lootTunnel:
                printSlowly ("You enter the tunnel. It is dark and quiet. You are safe for now...")
                printSlowly("You look around the area for loot...")
                if rollLoot():
                    lootNumber = random.randint(1,3)
                    if lootNumber == 1:
                        printSlowly("You find a small pouch of 10 gold on the floor.")
                        playerGoldCount += 10
                    if lootNumber == 2: 
                        printSlowly("You find a pouch of 25 gold on the floor. I wonder who left this here? ...")
                        playerGoldCount += 25
                    if lootNumber == 3:
                        printSlowly("You find a large gold nugget on the floor. It's worth at least 50 gold! You put it in your pouch.")
                        playerLoot.append("Gold Nugget")
                        playerGoldCount += 50
                else:
                    printSlowly("You find nothing of value.")
            # Safe Tunnel
            else:
                printSlowly ("You enter the tunnel. It is dark and quiet. You are safe for now...")

            
            #Continue on your way
            input("Press Enter to continue on your way. ")
            if playerTunnelCount >= 0:
                lastPlayerTunnelCount = playerTunnelCount
            playerTunnelCount += 1 # Increment tunnel count
            printSlowly("..............")
            
         
        # Check if the player has found the exit
        if playerTunnelCount >= TunnelExit:
            printSlowly("You see a light in the distance. You run towards it and find yourself outside. You have escaped the cave!")
            printSlowly("Congratulations! You have won the game!")
            if dragonDefeated:
                printSlowly("You defeated the dragon. Surely you are a hero now!")
            if trollDefeated:
                printSlowly("You defeated the troll. You've saved countless lives!")
            if goblinDefeated:
                printSlowly(f"You defeated the {goblinSlayCount} goblin(s). You are a true warrior!")
                gameOver = True
        else:
            printSlowly("You have died. Game Over.")
            gameOver = True
        
        printSlowly(f"You made it through {str(playerTunnelCount)} tunnels and found {playerGoldCount} gold.")
        if len(playerLoot) > 0:
            printSlowly(f"You found the following items: {str(playerLoot)}")

        
        while True:
            try:
                playAgain = input("Would you like to play again? (Enter anything to restart, or N to exit.) ")
                if playAgain.lower() == "n":
                    exit = True
                    break
                else:
                    printSlowly("Starting new game...")
                    print("---------------------------------------------")
                    print()
                    gameOver = False
                    break
            except:
                continue
            
        
        
            
