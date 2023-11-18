#Adventure Game John_Moreau
import random


print ("You are lost in a maze of underground tunnels.")
dangerTunnel = random.randint(1,2)

# tunnelChoice = int(input("There are two tunnels, which one do you take? (1 or 2)"))

while tunnelChoice > 2 or tunnelChoice < 1:
    if tunnelChoice == 3:
        print("You've found a secret tunnel! The moonlight shines through a crack in the ceiling, illuminating a large wooden chest. Open the chest, or turn around? (1 or 2)")
    tunnelChoice = int(input("There are only two tunnels, which one do you take? (1 or 2)"))
    
if tunnelChoice == dangerTunnel:
    print ("You enter the tunnel. Suddenly you hear a loud growl and see a pair of glowing eyes in the darkness. You've entered the tunnel with a dragon!")
else:
    print ("You enter the tunnel. It is dark and quiet. You are safe for now.")