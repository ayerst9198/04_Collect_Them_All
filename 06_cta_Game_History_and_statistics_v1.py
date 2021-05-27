# Functions go here

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
            print("Please input yes / no")

# loop code for testing purposes 
rounds = 0
while 1 == 1:
    rounds += 1
    cost_error = "Plese enter a number above 0"
    cost = num_check("How much does it cost? ", float, cost_error, 1)
    all_tokens = list("all the tokens generated ever")
    print()
    # prints the cost, displayed as a price
    print("Item Cost: $%3.2f"%(cost))
    print()
    rounds_played = num_check("How many times did you generate a token? ", int, "Please enter an int above 1", 2)
    print()
    history = yes_no("Do you want to see your history? ")
    print()
    total_cost = cost * rounds_played
    if history == "yes":
        print("You played {} rounds".format(rounds_played))
        print()
        print("The total cost is: $%3.2f"%(total_cost))
        print()
    
    statistics = yes_no("Do you want to see your statistics? ")
    if statistics == "yes":
        print("tokens genrated in round #{}: {}".format(rounds ,all_tokens))
        continue
    else:
        print()
        continue