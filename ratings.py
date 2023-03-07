"""Restaurant rating lister."""

# import the sys module

import sys

# assign the file name to a variable

filename = sys.argv[1]

# create empty ratings dictionary
ratings = {}

# define function to read file and return dictionary
def create_ratings_dict(filename):
    """ reads file, returns dict of restaurant name : rating """    

    #open file
    with open(filename) as file:

        # go through each line
        for line in file:

            # split line at colon to get restaurant and rating
            restaurant, rating = line.rstrip().rsplit(':')

            # make restaurant: rating a key value pair in the ratings dict
            ratings[restaurant] = int(rating)

    return ratings

# create ratings as universal dictionary
ratings = create_ratings_dict(filename)


def print_ratings():
    """ print current ratings alphabetically by restaurant """

    # iterate through each restaurant:rating pair
    for restaurant, rating in sorted(ratings.items()):

        # print statement regarding rating of restaurant
        print(f"{restaurant} is rated at {rating}")

    # return None
    return


def change_rating(restaurant):
    """change rating for a given restaurant"""

    # create while loop to validate data
    while True: 

        rating = input(f'What score do you want to give {restaurant}? ')

        if not rating.isdigit():
            print('Rating must be an integer between 1 and 5')

        elif 1 <= int(rating) <= 5:

            # update restaurant key in ratings dict with new rating
            ratings[restaurant] = rating

            # exit function
            return
        
        else:
            print('Rating must be an integer between 1 and 5')
        


        

def rate_restaurant():
    """ Rate a specific restaurant """

    restaurant = input("What restaurant do you want to rate? ")

    if restaurant in ratings:

        proceed = input(f'{restaurant} is already rated. Do you wish to change the rating? Y/N: ')
        
        if proceed.lower()[0] == 'n':

            print('OK, this request has been cancelled.')
            
            return

    change_rating(restaurant)

    return

def rate_random_restaurant():
    """ Rate a random restaurant"""

    # only import choice from random here; not needed if this function isn't called
    from random import choice 

    chosen_restaurant = choice(list(ratings))

    change_rating(chosen_restaurant)

    return

def help_user():
    """prints choices"""
    
    print('Your choices are:')
    print('1: See the ratings in alphabetical order')
    print('2: Add or update restaurant rating')
    print('3: Update a random restaurant rating')
    print('4: Quit')
    print('Help: Print this list again')
    
    return

def let_user_choose():
    """ Let user navigate program """
    
    help_user()
    
    while True:
        choice = int(input("Choose 1, 2, 3, 4, or Help: "))
        
        if choice == 1:
            print_ratings()

        elif choice == 2:
            rate_restaurant()

        elif choice == 3:
            rate_random_restaurant()
            
        elif choice == 4:
            # quit
            return
        
        elif choice[0].lower() == 'h':
            help_user()

        else: 
            print('I\'m sorry, that is not a valid option.')


let_user_choose()


