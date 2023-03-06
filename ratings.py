"""Restaurant rating lister."""


# import the sys module

import sys

from random import choice 

# assign the open file to a variable

filename = sys.argv[1]

# define function to read file and return dictionary
def file_to_dict(filename):
    
    """ This function reads the file and gives the ratings in the dict format

        Input is filename
        return the rating in the dict """

    with open(filename) as lines:

        ratings = {}

        for line in lines:

            restaurant, rating = line.rstrip().rsplit(':')
            ratings[restaurant] = int(rating)

    return ratings


def print_rest_ratings(ratings):

    for restaurant, rating in sorted(ratings.items()):

        print(f"{restaurant} is rated at {rating}")

    return


def get_new_rating(ratings):

    restaurant = input("What restaurant do you want to rate? ")

    while True:
        
        try:    
            rating = int(input("What score do you want to give it? (integer, 1-5) "))
            if 1 <= rating <= 5:
                break
            # raise error
            # else:
            #     raise 'incorrect' **why doesn't this work?**

        except ValueError or not 1 <= rating <= 5:

            print("Enter an integer value between 1 and 5")

    ratings[restaurant] = rating

    print_rest_ratings(ratings)

    return


def update_random_rating(ratings):

    chosen_restaurant = choice(list(ratings))

    print(f'The restaurant is {chosen_restaurant} and the current rating is {ratings[chosen_restaurant]}')

    ratings[chosen_restaurant] = int(input("What do you want the new rating to be?: "))

    print(f'The new rating for {chosen_restaurant} is {ratings[chosen_restaurant]}')
    return ratings

def update_specific_rating(ratings):
    
    restaurant = input("What restaurant do you want to update? ")

    print(f'The restaurant is {restaurant} and the current rating is {ratings[restaurant]}')

    new_rating = int(input(f"What is your updated rating for the restaurant {restaurant}"))

    if restaurant in ratings:
    
        ratings[restaurant] = new_rating
        print_rest_ratings(ratings)
    
    else:

        print("The restaurant is not in the list , Do you want to add")
        get_new_rating(ratings)
    
    return


def let_user_choose():
    print('Your choices are:')
    print('(1) See the ratings in alphabetical order')
    print('(2) Add a new restaurant rating')
    print('(3) Update a random restaurant rating')
    print('(4) Update a specific restaurant rating')
    print('(5) Quit')
    
    while True:
        choice = int(input("Choose 1, 2, 3, 4, or 5: "))
        ratings = file_to_dict(filename)
        if choice == 1:
            # see ratings
            #ratings = file_to_dict(filename)
            print_rest_ratings(ratings)
        elif choice == 2:
            #ratings = file_to_dict(filename)
            get_new_rating(ratings)

        elif choice == 3:
            update_random_rating(ratings)
            
        elif choice == 4:
            update_specific_rating(ratings)
            
        elif choice == 5:
            # quit
            return
        else: 
            print('I\'m sorry, you need to choose 1, 2, or 3.')

let_user_choose()

# create function to store ratings in a dictionary

# rest_ratings = file_to_dict(filename)

# print the ratings in alphabetical order by restaurant

# print_rest_ratings(rest_ratings)

# prompt input from user

# get_new_rating(rest_ratings)
