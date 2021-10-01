def main_menu():
    # Print instructions and intro
    print("Tom(cat) and Jerry(mouse) in Wisconsin cheese factory Text Adventure Game")
    print("Collect different cheeses from different country room to win the game, or be killed by the cat.")
    print("Move commands: go South, go North, go East, go West")
    print("Add cheese to your basket: get 'cheese name'")


def move_between_rooms(current_room, move, rooms):
    # move to corresponding room
    current_room = rooms[current_room][move]
    return current_room


def get_cheese(current_room, move, rooms, basket):
    # add cheese to basket and remove it from the room
    basket.append(rooms[current_room]['cheese'])
    del rooms[current_room]['cheese']


def main():
    # dictionary of connecting rooms with items
    rooms = {
        'Production room': {'South': 'Mexico', 'North': 'Greece', 'East': 'South Asia', 'West': 'Kitchen'},
        'Mexico': {'North': 'Production room', 'East': 'Ethiopia', 'West': 'Mus musculus', 'cheese': 'Cotija'},
        'Ethiopia': {'West': 'Mexico', 'cheese': 'Ayibe'},
        'Mus musculus': {'East': 'Mexico', },
        'South Asia': {'North': 'France', 'West': 'Production room', 'cheese': 'Paneer'},
        'France': {'South': 'South Asia', 'cheese': 'Camembert'},
        'Kitchen': {'East': 'Production room', 'cheese': 'Tom'},
        'Italy': {'East': 'Greece', 'cheese': 'Burrata'},
        'Greece': {'East': 'England', 'South': 'Production room', 'cheese': 'Feta'},
        'England': {'West': 'Greece', 'cheese': 'Cheddar'}

    }

    # list for storing player basket
    basket = []
    # starting room
    current_room = "Mus musculus"
    # show the player the main menu
    main_menu()

    while True:
        # When jerry encounters the Tom
        if current_room == 'Kitchen':
            # winning case
            if len(basket) == 8:
                print('Congratulations Jerry you have defeated Tom and saved your family')
                print('Thank you for playing!')
                break
            # losing case
            else:
                print('\nOh nooooo Jerry, You did not collect all of the cheese!')
                print('You were killed by Tom')
                print('Thank you for playing!')
                break
        # Tell the user their current room, basket and prompt for a move, ignores case
        print('You are in the ' + current_room)
        print(basket)
        # tell the user if there is a cheese in the room
        if current_room != 'Kitchen' and 'cheese' in rooms[current_room].keys():
            print('You see the {}'.format(rooms[current_room]['cheese']))
        print('------------------------------')
        move = input('Where do you want to go: ').title().split()
        print(move)

        # handle if the user enters a command to move to a new room
        if len(move) >= 2 and move[1] in rooms[current_room].keys():
            current_room = move_between_rooms(current_room, move[1], rooms)
            continue
        # handle if the user enter a command to get an item
        elif len(move[0]) == 3 and move[0] == 'Get' and ' '.join(move[1:]) in rooms[current_room]['cheese']:
            print('You pick up the {}'.format(rooms[current_room]['cheese']))
            print('------------------------------')
            get_cheese(current_room, move, rooms, basket)
            continue
        # handle if the user enters an invalid command
        else:
            print('Invalid move, please try again')
            continue


main()
