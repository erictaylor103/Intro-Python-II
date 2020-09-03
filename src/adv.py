from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Shovel", "Digs up treasures")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Hand sanitizer", "Keeps your hands clean")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Gold Coins", "Makes you Rich!")]),
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
player1 = Player("Eric", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
print("\n")
print(f"Welcome {player1.name}, to your adventure!")
while True:
    current_room = player1.location
    #print("\n")
    print("-----------------------------------------------")
    print("\n")
    print(f"Current Room: {player1.location.name}")
    print(f"Description: {player1.location.description} \n")    
    player_input = input("Which way now?: [n]North, [s]South, [e]East, [w]West, [i]Edit Inventory, [q]Quit Game: ")    
    print("-----------------------------------------------")

    #if the player enters "i":
    #open the inventory to view Inventory or to remove items from inventory
    if player_input == "i":
        edit_inventory = False
        while edit_inventory is False:            
            edit_inventory_prompt = input(f"View/Edit Inventory? [y]Yes / [n]No: ")
            if edit_inventory_prompt == "y":
                edit_inventory = True
                inventory_list = player1.items.copy()

                ######Show Inventory details for player1
                inventory_list = []
                for item in player1.items:
                    inventory_list.append(item.name)
                print(f"Player Inventory: {str(inventory_list)[1: -1]}")

                #for item in inventory_list:
                #    total_inventory.append(item.name) 
                #print(f"Inventory: {str(total_inventory)}") #####check why it is not printing a string version of inventory_list                   
                for item in player1.items:
                    remove_prompt = input(f"Remove {item.name}? [y]Yes / [n]No: ")
                
                    if remove_prompt == "y":
                        player1.items.remove(item)
                        player1.location.items.append(item)
                    print(f"New Inventory List: {player1.items}")
                    
            elif edit_inventory_prompt == "n":
                #print(f"Player Inventory: {str(inventory_list)[1: -1]}")
                edit_inventory = True
            else:
                pass
    
# If the user enters a cardinal direction, attempt to move to the room there.
    if player_input == "n":
        if current_room.n_to is not None:
            player1.location = current_room.n_to
            print("\n")
            print("You chose North")
        else:
            print("|||||You can't go that way...Try another Direction|||||")
    
    elif player_input == "s":
        if current_room.s_to is not None:
            player1.location = current_room.s_to
            print("\n")
            print("You chose South")
        else:
            print("|||||You can't go that way...Try another Direction|||||")
    
    elif player_input == "e":
        if current_room is not None:
            player1.location = current_room.e_to
            print("\n")
            print("You chose East")
        else:
            print("|||||You can't go that way...Try another Direction|||||")
    
    elif player_input == "w":
        if current_room is not None:
            player1.location = current_room.w_to
            print("\n")
            print("You chose West")
        else: 
            print("|||||You can't go that way...Try another Direction|||||")
    
    
    elif player_input == "q":
        print("You've quit the adventure...see ya another time! \n \n")
        exit()
    
    else:
        print("Please make sure you only choose one of the following: [n]North, [s]South, [e]East, [w]West, [q]Quit Game: \n")
# Print an error message if the movement isn't allowed.

####check if the location (current_room) has items
####if it has items:
                    #show the player the items found
                    #give the player the option to pick up the items
                    #add the items to the player1 items list
                    #remove the picked up items from player 1 location items
    if len(player1.location.items) != 0:
        items_list = player1.location.items.copy()

        for item in items_list:
            item_picked_up = False
            print(f"You found: {item.name} / Power: {item.description}")

            while item_picked_up is False:
                pick_up_prompt = input("Pick up item? [y]Yes - [n]No: ")
                
                if pick_up_prompt == "y":
                    #append(add) the picked up item to the palyer1 items list
                    player1.items.append(item)
                    #remove the picked up item from the room items list
                    player1.location.items.remove(item)
                    item_picked_up = True
                
                elif pick_up_prompt == "n":
                    item_picked_up = True
        else:
            pass
    
    else:
        print("\n")
        print("There are no items in this room")
    
#
# If the user enters "q", quit the game.
