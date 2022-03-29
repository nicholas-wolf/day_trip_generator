

import random


destinations_list = ["Atlanta", "New York", "Paris", "London"]
restaurant_list = ["McDonald's", "Burger King", "Taco Bell", "Subway"]
transportation_list = ["Car", "Scooter", "Bicycle", ]
entertainment_list = ["Museum", "Walk through park", "Movies"]


# Takes in list, checks lenght of list, and generates a random number based on length of list, and then removes that item in the list based on the random number
def random_list_item(passed_in_list):
    num = len(passed_in_list)
    randomNum = random.randrange(0, num, 1)
    item = passed_in_list.pop(randomNum)
    return item
   

# Gives Choices from given list for user to choose from
def choice_selector(choice_list, text):
    new_suggestion = random_list_item(choice_list)
    user_choice = input("We have selected " + new_suggestion + " would you like to keep this " + text + "? Enter y/n: " )

    while user_choice != "y": 
        if choice_list:
            new_suggestion = random_list_item(choice_list)
            user_choice = input("Ok no problem, we will select a new " + text + ", " + new_suggestion + " would you like to keep this new " + text + "? Enter y/n: " )
        else:
            print("We have ran out of " + text + " to suggest to you.")
            return ""
    return new_suggestion


## MAIN FUNCTION to select a trip for user
def welcome_trip_generator():
    welcome_day_trip_generator = "Welcome to your day trip generator, we will help you choose your trip!"
    print(welcome_day_trip_generator)

    destination = choice_selector(destinations_list, "destination")

    if destination != "":
        restaurant = choice_selector(restaurant_list, "restaurant")
        if restaurant != "":
            transportation = choice_selector(transportation_list, "transportation")
            if transportation != "":
                entertainment = choice_selector(entertainment_list, "entertaiment")
                if entertainment != "":
                    print("You went to  " + destination + ", and eat at " + restaurant + ", and traveled by " + transportation + ", and did " + entertainment + ".")
                else:
                    no_vacay()
            else:
                no_vacay()
        else:
            no_vacay()
    else:
        no_vacay()



welcome_trip_generator()

