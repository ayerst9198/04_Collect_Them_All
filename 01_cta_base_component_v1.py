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

def instructions():
    print(
        "Welcome to Collect them all, this program\n"
        "allows you to choose an item that will be\n"
        "purchased along with a token. These token\n"
        "will be able to spell out the item you chose\n"
        "and when you can spell it out you get a reward.\n"
        "This Program calculates how much it costs.\n"
        "to recieve all the tokens.\n"
        "Please Enjoy"
        
    )
    print()
    return""
# Main routine goes here

play_again = "yes"
while play_again == "yes":
    print()
    statement_generator("Welcome to Collect Them All", "|", "-")
    show_instructions = yes_no("Do you want to see your instructions? ")
    print()
    if show_instructions == "yes":
        statement_generator("Instructions", "|", "?")
        print()
        instructions()
    # asks user for a product name
    word = word_check("Enter a product name please: ", "Too few characters")
    print() 
    statement_generator("The product is {}".format(word), "|", "~")
    
    print() 

    # puts word into list and prints the list
    word_list = list(word)
    comp_list = word_list
    tries = 0

    # Asks user for the cost of the product
    cost_error = "Plese enter a number above 0"
    cost = num_check("How much does it cost? ", float, cost_error, 1)
    print()
    # prints the cost, displayed as a price
    statement_generator("Item Cost: $%3.2f"%(cost), "-", "-")
    print()
    while comp_list != []:
        token = random.choice(word_list)
        statement_generator("You got the {} token".format(token), "-", "")
        tries += 1
        total_cost = tries * cost
        if token in comp_list:
            comp_list.remove(token)
            word_list = list(word)
        if comp_list == []:
            statement_generator("You got ALL the tokens", "!", "*")
            print()
            print("You win a free {}!".format(word))
            print()
            print("You bought {} {}s and it cost you ${}".format(tries, word, total_cost))
            print()
            play_again = yes_no("Do you want to participate again? ")
            break
        print("Tokens left: {}".format(comp_list))
        next_round = input("")
        print()