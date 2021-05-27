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


while 1 == 1:
    show_instructions = yes_no("Do you want to see your instructions? ")
    print()
    if show_instructions == "yes":
        print("show instructions")
        print()
        print("program continues")
        print()
    else:
        print("program continues")
        print()