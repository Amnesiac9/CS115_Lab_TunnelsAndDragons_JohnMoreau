#Adventure Game John_Moreau
import random


# Declare Global Variables
exit = False
gameOver = False
TunnelExit = 5
dragonThreshold = 15
trollThreshold = 10
goblinThreshold = 5


# Define a function to roll a D20
def rollD20(threshold, bonus) -> int:
    print("You roll a D20. You must roll a ", str(threshold), " or higher.")
    roll = random.randint(1,20)
    print("You roll a: ", str(roll), " + ", str(bonus), ".")
    return roll + bonus

# Main Game Loop
while not exit:
    
    # Main Menu
    print("Welcome to the Adventure Game!")
    print("1. Start Game")
    print("2. Exit")
    menuChoice = int(input("What would you like to do? (1 or 2)"))
    while menuChoice > 2 or menuChoice < 1:
        menuChoice = int(input("What would you like to do? (1 or 2)"))
    if menuChoice == 2:
        exit = True
        break
    
    # Start Game
    while not gameOver:
        
        # New Game
        # Player Variables
        playerWeapons = False
        secretTunnelFound = False
        playerRollBonus = 0
        playerTunnelCount = 0
        
        print("It's dark and quiet. The cold stone walls are damp and covered in moss and slime.")
        print("You sit up off your back and feel around in the darkness for your torch and equipment.")
        print("You find your torch and light it. You are in a small room with two tunnels in front of you.")
        print ("You appear to be lost in an underground cave. You must find your way out.")
        
        # While the player has not found the exit
        while playerTunnelCount < TunnelExit:
            
            if gameOver:
                break
            
            tunnelChoice = int(input("There are two tunnels in front of you, which one do you take? (1 or 2)"))
            dangerTunnel = random.randint(1,3)
            secretTunnel = random.randint(1,3)

            # Get tunnel choice
            while tunnelChoice > 2 or tunnelChoice < 1:
                # if tunnelChoice == 4:
                #     secretTunnelFound = True
                #     break
                tunnelChoice = int(input("There are only two tunnels, which one do you take? (1 or 2)"))
                
            # Check result of tunnel choice
            if tunnelChoice == dangerTunnel:
                print ("You enter the tunnel. Suddenly you hear a loud growl and see a pair of glowing eyes in the darkness. You've entered the tunnel with a dragon!")
                if playerWeapons:
                    playerRollBonus = 7
                #Roll a D20 to see if the player can defeat the dragon 
                playerRoll = rollD20(dragonThreshold, playerRollBonus)
                if playerRoll < dragonThreshold:
                    print ("The dragon leaps out of the darkness and swallows you whole. The world starts to fade.")
                    gameOver = True
                    continue
                elif playerWeapons:
                    print("The dragon lets out a loud roar and unleashes a jet of fire at you. You raise your shield and deflect the flames. You charge at the dragon and stab it in the chest.")
                    print("The dragon lets out a loud roar and falls to the ground in a large plume of dust and smoke.")
                    print ("You defeat the dragon and continue on your way.")
                else:
                    print("The dragon lets out a loud roar and unleashes a jet of fire at you. You roll out of the way and the flames hit the wall behind you. You run back the way you came.")
                    print ("You escape the dragon and continue on your way.")
                    playerTunnelCount -= 1 # Go back one tunnel
                        
            # Check if the player has found the secret tunnel
            elif tunnelChoice == secretTunnel:
                print ("You learn against the wall to rest. Suddenly you hear a loud click and the wall opens up to a secret tunnel!")
                print ("In front of you is a large wooden chest illuminated by moonlight from a crack in the cave cieling above.")
                chestChoice = int(input("Do you open the chest? (1) Yes, (2) No"))
                
                while chestChoice > 2 or chestChoice < 1:
                    chestChoice = int(input("Do you open the chest? (1) Yes, (2) No"))
                if chestChoice == 1:
                    trappedChest = 5
                    playerRoll = rollD20(5)
                    if playerRoll < trappedChest:
                        print ("You open the chest, somewhere you hear a stone move. A dart shoots out of the darkness and hits you in the back. You fall over and the world starts to fade.")
                        break
                    else:
                        print ("You open the chest. Inside is a thick layer of black soot and dust. You find a steel sword with a ruby embeded in the hilt, and metal shield with a fire emblem. You equip them and continue on your way.")
                        playerWeapons = True
            else:
                print ("You enter the tunnel. It is dark and quiet. You are safe for now. You continue on your way.")
                
            #Increment tunnel count, continue to the exit.
            playerTunnelCount += 1
         
        # Check if the player has found the exit
        if playerTunnelCount >= TunnelExit:
            print ("You see a light in the distance. You run towards it and find yourself outside. You have escaped the cave!")
            print ("Congratulations! You have won the game!")
            gameOver = True
            continue       
            
