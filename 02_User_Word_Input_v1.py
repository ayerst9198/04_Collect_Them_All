# functions go here
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

# loop for testing
# asks user for a word, prints word
word = word_check("enter word please: ", "Too few characters")
print() 
print(word)
print() 

# puts word into list and prints the list
word_list = list(word)
print(word_list)