from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player("eric", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

while True:
    current_room = player1.location
    print(f"You are currently in room: {current_room.name}")
    print(f"Your room description: {current_room.description} \n")

    player_input = input("Enter your next move: n, s, e, w or q to quit:")
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

    if player_input == "n":
        if current_room.n_to is not None:
            player1.location = current_room.n_to
            print(f"You chose North.")
        else:
            print(f"There is no available room there. Try another direction! \n")
    
    elif player_input == "s":
        if current_room.s_to is not None:
            player1.location = current_room.s_to
            print(f"You chose South")
        else:
            print("There is no available room there. Try another direction! \n")
    
    elif player_input == "w":
        if current_room.w_to is not None:
            player1.location = current_room.w_to
            print(f"You chose West")
        else:
            print("There is no available room there. Try another direction! \n")
    
    elif player_input == "e":
        if current_room.e_to is not None:
            player1.location = current_room.e_to
            print ("You chose East")
        else:
            print("There is no available room there. Try another direction! \n")
    
    elif player_input == "q":
        print ("You selected to quit the game. Bye!")
        exit()
    
    else:
        print("Please make sure you only choose one of the following: n, s, e, w or q to quit: \n")
        


        