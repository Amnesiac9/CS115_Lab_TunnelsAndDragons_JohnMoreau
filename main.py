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
    input(f"Press Enter to roll a D20. You must roll a {str(threshold)} or higher. ")
    roll = random.randint(1,20)
    printSlowly(f"You roll {str(roll)} + {str(bonus)} bonus from your equipment.")
    input("Press Enter to continue.")
    if roll + bonus >= threshold:
        return True
    else:
        return False

def rollEscape(diceSize) -> bool:
    input(f"Press Enter to roll a D{str(diceSize)}. You must roll a 2 or higher. ") 
    if random.randint(1,diceSize) > 1:
        return True
    else:
        return False

def rollLoot() -> bool:
    lootRollThreshold = random.randint(4,8)
    return rollD20(lootRollThreshold, getPlayerRollBonus("loot"))
     

def getPlayerRollBonus(type) -> int:
    playerRollBonus = 0
    
    if type == "combat":
        if playerWeaponsFound:
            playerRollBonus += 6
        if dragonScaleFound:
            playerRollBonus += 3
        if boneToothFound:
            playerRollBonus += 3
        if emeraldRingFound:
            playerRollBonus += 1
    else: # Loot
        if dragonScaleFound:
            playerRollBonus += 2
        if sapphireAmuletFound:
            playerRollBonus += 4
        if emeraldRingFound:
            playerRollBonus += 2

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
        trappedChestThreshold = random.randint(4,6)
        TunnelExit = random.randint(8,12)
        # lootRollThreshold = 
        # Player Variables
        playerWeaponsFound = False
        secretTunnelFound = False
        dragonDefeated = False
        trollDefeated = False
        goblinDefeated = False
        dragonScaleFound = False
        sapphireAmuletFound = False
        boneToothFound = False
        emeraldRingFound = False
        glowingCrystalFound = False
        playerLootRollBonus = 0
        playerCombatRollBonus = 0
        lastPlayerTunnelCount = 0
        playerTunnelCount = 0
        playerLoot = []
        playerGoldCount = 0
        goblinSlayCount = 0
        firstTurn = True
        
        
        # While the player has not found the exit
        while playerTunnelCount < TunnelExit:
            
            if gameOver:
                break

            # Roll for tunnel contents
            if playerTunnelCount == TunnelExit - 1 or playerTunnelCount == TunnelExit - 2:
                dragonTunnel = random.randint(1,2) # 50% chance of dragon, dragon takes precedence over other enemies and loot
                trollTunnel = random.randint(1,9) # Enemies take precedence over loot
                goblinTunnel = random.randint(1,6) # Enemies take precedence over loot
                lootTunnel = random.randint(1,2) # 50% chance of loot
            else:
                dragonTunnel = random.randint(1,32)
                trollTunnel = random.randint(1,9)
                goblinTunnel = random.randint(1,6)
                lootTunnel = random.randint(1,4)
                if secretTunnelFound:
                    secretTunnel = 0 # Turn off secret tunnel
                else:
                    secretTunnel = random.randint(1,4)
            
            
            # Check if the player went back a tunnel
            if playerTunnelCount == lastPlayerTunnelCount and not firstTurn:
                printSlowly("The two tunnels look different from before...")
            
            # Update last tunnel count for next turn
            lastPlayerTunnelCount = playerTunnelCount
            
            tunnelChoice = 0
            # Get tunnel choice
            while tunnelChoice > 2 or tunnelChoice < 1:
                try:
                    tunnelChoice = int(input("There are two tunnels in front of you, which one do you take? (1 or 2): "))
                except:
                    continue
            
            
            firstTurn = False # Used to check if it's the first turn
            safeTunnel = False # Used to check if the player is in a safe tunnel
            
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
                        playerWeaponsFound = True
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
                printSlowly ("You enter the tunnel. Suddenly you hear a low rumbling growl and see a pair of huge glowing eyes in the darkness. You've entered the tunnel with a dragon!")
                
                #If the player has weapons, they can choose to attack the dragon
                if playerWeaponsFound:
                    attackChoice = 0
                    while attackChoice > 2 or attackChoice < 1:
                        try:
                            attackChoice = int(input("Do you (1) Attack the dragon, or (2) Try to run away?: "))
                        except:
                            continue
                    if attackChoice == 1:
                        printSlowly("You raise your shield and sword to fight.")
                        printSlowly("The dragon lets out a loud roar and unleashes a jet of fire at you. You raise your shield and deflect the flames. You charge at the dragon and stab it in the chest.")
                        if rollD20(dragonThreshold, getPlayerRollBonus("combat")):
                            printSlowly("The dragon lets out a thundering roar and falls to the ground in a large plume of dust and smoke.")
                            printSlowly ("You defeat the dragon.")
                            dragonDefeated = True
                        else:    
                            printSlowly("The dragon's scales are too thick and your sword bounces off, the dragon turns to face you.")
                            if glowingCrystalFound:
                                printSlowly("You think quickly, and remember the glowing crystal in your pouch.")
                                printSlowly("The dragon lets out a loud roar and unleashes another jet of fire at you.")
                                printSlowly("You raise the glowing crystal in your hand and the flames are absorbed into it. You feel the crystal grow hot in your hand.")
                                printSlowly("You throw the crystal at the dragon just as it starts to burn your hand. The crystal explodes in a blinding flash of cold light.")
                                printSlowly("The room goes silent. As the smoke and dust clears you see the dragon has been frozen solid. The large cavern room is chilled.")
                                printSlowly("You walk over to the dragon and stab it in the chest with your sword. The dragon shatters into a million pieces of ice.")
                                printSlowly ("You defeat the dragon.")
                                dragonDefeated = True
                            elif rollEscape(3): # 1/3 chance to lose game, 2/3 chance to escape
                                printSlowly("The dragon lets out a loud roar and unleashes another jet of fire at you.")
                                printSlowly("You narrowly roll out of the way and the flames hit the wall behind you. Your fighting spirit has left you. You run back the way you came.")
                                printSlowly ("You narrowly escape the dragon.")
                                playerTunnelCount -= 1 # Go back one tunnel
                            else:
                                printSlowly("The dragon lets out a deafening roar and unleashes another jet of fire at you.")
                                printSlowly ("Your shield drops to the ground as the flames engulf you. The world starts to fade.")
                                gameOver = True
                                continue
                        if dragonDefeated:
                            printSlowly("You look around the area for loot...")
                            goldRoll = random.randint(100,250)
                            printSlowly(f"You find the dragon's hoard of gold it was guarding... there's too much to carry, but you manage to stuff {goldRoll} gold pieces into your pockets.")
                            playerGoldCount += goldRoll
                            printSlowly("You also find a small red shimmering pearlescent scale on the floor. You feel the heat as you pick it up, it warms your hands and fills you with a strong sense of fighting spirit. You put it in your side pouch.")
                            dragonScaleFound = True
                            playerLoot.append("Dragon Scale")
                # If the player does not have weapons, they can try to run away
                else:
                    printSlowly("You attempt to run away...")
                    if rollEscape(3):
                        printSlowly("The dragon lets out a loud roar and unleashes a jet of fire at you. You roll out of the way and the flames hit the wall behind you. You run back the way you came.")
                        printSlowly ("You escape the dragon.")
                        playerTunnelCount -= 1 # Go back one tunnel
                    else:
                        printSlowly ("The dragon leaps out of the darkness and swallows you whole. The world starts to fade.")
                        gameOver = True
                        continue
                    
            # Troll Tunnel   
            elif tunnelChoice == trollTunnel and trollDefeated == False:
                printSlowly ("You enter the tunnel. Suddenly you hear a low rumbling slow growl. A large creature towers over you. You've entered the tunnel with a troll!")
                #Roll a D20 to see if the player can defeat the troll or escape
                if not rollD20(trollThreshold, getPlayerRollBonus("combat")):
                    if not rollEscape(4):
                        printSlowly ("The troll leaps out of the darkness and smashes you with a wooden club. The world starts to fade.")
                        gameOver = True
                        continue
                    else:
                        printSlowly("The troll lets out a loud roar and charges at you. You roll out of the way and the troll hits the wall behind you, dazed. You run back the way you came.")
                        printSlowly ("You narrowly escape the troll.")
                        playerTunnelCount -= 1 # Go back one tunnel
                elif playerWeaponsFound:
                    printSlowly("The troll lets out a loud roar and charges at you. You raise your shield and sword to fight. You roll to dodge the trolls attack and stab it squarely in the ribs.")
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
                    if not rollEscape(6):
                        printSlowly ("The goblin leaps out of the darkness and stabs you with a rusty dagger. The world starts to fade.")
                        gameOver = True
                        continue
                    else:
                        printSlowly("The goblin lets out a loud screetch and charges at you. You roll out of the way and the goblin stabs the empty air where you stood just moments before. You run back the way you came.")
                        printSlowly ("You narrowly escape the goblin.")
                        playerTunnelCount -= 1 # Go back one tunnel
                elif playerWeaponsFound:
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
                            printSlowly("You also find a large bone tooth on a leather strap around the goblin's wrist. You remove the charm and place it on your arm. You feel a surge of fighting spirit.")
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
                    while True:
                        lootNumber = random.randint(1,5)
                        if lootNumber == 1:
                            printSlowly("You find a small pouch of 10 gold on the floor.")
                            playerGoldCount += 10
                            break
                        if lootNumber == 2: 
                            printSlowly("You find a pouch of 25 gold on the floor. I wonder who left this here? ...")
                            playerGoldCount += 25
                            break
                        if lootNumber == 3:
                            printSlowly("You find a large gold nugget on the floor. It's worth at least 50 gold! You put it in your pouch.")
                            if playerLoot.count("Gold Nugget") == 0:
                                playerLoot.append("Gold Nugget")
                            else:
                                playerLoot.append(f"Gold Nugget x{playerLoot.count('Gold Nugget') + 1}")
                                playerLoot.remove("Gold Nugget")
                            playerGoldCount += 50
                            break
                        if lootNumber == 4 and not glowingCrystalFound:
                            printSlowly("You see a glowing object in the distance. You walk towards it and find a small glowing crystal. It feels cold to the touch. You put it in your pouch.")
                            playerLoot.append("Glowing Crystal")
                            glowingCrystalFound = True
                            break
                        if lootNumber == 5 and not emeraldRingFound:
                            printSlowly("You find a small wooden box on the floor partially burried beneath some rubble.")
                            printSlowly("You open it and find a small silver ring with an emerald embeded in the center. You put it on your finger for good luck.")
                            playerLoot.append("Silver Emerald Ring")
                            emeraldRingFound = True
                            break
                else:
                    printSlowly("You find nothing of value.")
            # Safe Tunnel
            else:
                safeTunnel = True
                printSlowly ("You enter the tunnel. It is dark and quiet. You are safe for now...")

            
            #Continue on your way
            if not safeTunnel:
                input("Press Enter to continue on your way. ")
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
                if playAgain.strip().lower() == "n":
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
            
        
        
            
