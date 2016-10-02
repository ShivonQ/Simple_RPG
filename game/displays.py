'''These are all 80 characters long'''
def display_base_hero_options():
    print('|   1) Find a Merchant 2) Drink a Potion 3) Rest 4) Explore  5) Save/Quit Game |')


def display_fight_menu():
    print('|   1) Attack   2) Drink Potion   3) Check Hero Status    4) Flee the Battle   |')


def display_merchant_menu():
    print('PLACEHOLDER STATEMETN FOR FREDS MERCHANT')


def display_rest_menu():
    print('|    1) Drink a Potion Before Bed          2) Go to Bed                        |')

def display_explore_menu():
    # in the future this will allow more location based exploration. like how that Mos Eisley game
    # had a simple console map, and certain areas were too dangerous to go to etc...
    print('|    1) Continue Exploring     2) Drink a Potion  3)   Camp for the Night      |')


def display_root_menu():
    print(' __________________________________SIMPLE RPG__________________________________ \n'
          '|   1) New Game     2) Open Saved Game     3) Enter Admin Section    4) Quit   |')


#     This method will eventually be able to reactively change strings based on the players name to fit 80 chars
def modify_string_for_display(string):
    length = len(string)
    difference = 0
    if length<80:
        difference = 80-length
