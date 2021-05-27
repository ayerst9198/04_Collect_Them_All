import random
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


key_word = word_check("What is the product? ", "Please enter a product name")
word_list = list(key_word)
print(word_list)
complete_list = []
token_trash = []

while 1 == 1:
    token = random.choice(word_list)
    print(token)

    if token in complete_list:
        token_trash.append(token)
        
    else:
        complete_list.append(token)
        token_trash.append(token)
    
    if word_list == complete_list:
        break
    print(complete_list)
    print(token_trash)

    play = input("")
print("congratulations")