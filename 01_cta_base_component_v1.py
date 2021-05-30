import random
import math

# Functions go here

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("<error> Unknown Answer "
                  "Detected. Please Input Yes/No")


def word_check(question, error):
    valid = False
    while not valid:

        response = input(question)

        # checks word length
        if len(response) < 2:
            print(error)
            continue
        else:
            return response


def num_check(question, num_type, error, low=None, high=None, exit_code=None):

    valid = False
    while not valid:
        try:
            response = input(question).lower()


            if response == exit_code:
                return response

            else:
                response = num_type(response)
 
            if low is not None and high is not None:
                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if response >= low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif high is not None:
                if response <= high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()


def statement_generator(statement, side_decoration, top_bottom_decoration):


    sides = side_decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = top_bottom_decoration * len(statement)


    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# Main routine goes here

play_again = "yes"
while play_again == "yes":
    show_instructions = yes_no("Do you want to see your instructions? ")
    print()
    if show_instructions == "yes":
        statement_generator("Instructions", "|", "?")
        print()
        print("program continues")
        print()
    else:
        print("program continues")
        print()
    # asks user for a product name
    word = word_check("Enter a product name please: ", "Too few characters")
    print() 
    print("The product is {}".format(word))
    
    print() 

    # puts word into list and prints the list
    word_list = list(word)
    comp_list = word_list

    # Asks user for the cost of the product
    cost_error = "Plese enter a number above 0"
    cost = num_check("How much does it cost? ", float, cost_error, 1)
    print()
    # prints the cost, displayed as a price
    print("Item Cost: $%3.2f"%(cost))
    print()
    rounds_error = "please enter an int above 0"
    rounds_allowed = num_check("How many rounds? ", int, rounds_error ,1)
    print()
    round = 1
    while rounds_allowed > 0:
        statement_generator("Round: {}".format(round), "|", "-")
        print()
        while comp_list != []:
            token = random.choice(word_list)
            print("You got the {} token".format(token))
            if token in comp_list:
                comp_list.remove(token)
            if comp_list == []:
                break
            print()
            print("Tokens left: {}".format(comp_list))
            print()
            next_round = input("")
            print()
            
        round += 1
        rounds_allowed -= 1