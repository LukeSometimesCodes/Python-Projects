

def start():
    fname = 'Luke'
    lname = 'Morreale'
    age = 22
    gender = 'Male'
    get_info (fname, lname, age, gender)



def get_info(fname, lname, age, gender):
    print ('My name is {} {}. I am a {} year old {}.'.format(fname, lname, age,gender))




def start1 (nice=0,mean=0,name=''):
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)


def describe_game(name):
    """
    check if this is a new game or not.
    If it is new, get the user's name.
    If it is not a new game, thank the player for
    playing again and continue with the game
    """
    #meaning, if we do not already have this user's name,
    #then they are a new player and we need to get their name
    if name != "":
        print('\nThank you for playing again, {}!'.format(name))
    else:
            stop = True
            while stop:
                if name == "":
                    name = input('\nWhat is your name? \n>>>'.capitalize())
                    if name != '':
                        print('\nWelcome, {}!'.format(name))
                        print('\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean')
                        print('but at the end of the game your fate \nwill be sealed by your actions.')
                        stop = False
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input('\nA stranger approaches you for a \nconversation. Will you be nice \n or mean? (N/M) \n>>>: ').lower()
        if pick == 'n':
            print('\nHad a nice conversation with the stranger')
            nice = (nice + 1)
            stop = False
        if pick == 'm':
            print ('\nDoes not have a conversation with the stranger')
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass the 3 variables to the score()



def show_score (nice,mean,name):
    print ('\n{}, your current total: \n({}, Nice) and ({}, Mean)'.format(name,nice,mean))             



def score(nice,mean,name):
    #score function is being passed the values stored within the 3 variables
    if nice > 2: #if condition is valid, call win function passing in the variables so it can use themm
        win(nice,mean,name)
    if mean > 2: #if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    #Substitutes the {} variable with out variable values
    print ('\nNice job {}, you win! \nYou pickde the same thing 3 times and won!'.format(name))
    #call again function and pass in our variables
    again(nice,mean,name)


def lose(nice,mean,name):
    #changes the {} wildcards with our variable values
    print('\ni hate you i hate you i hate you i hate you')
    #call again function and pass in our variables
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input('\nDo you want to play again? (y/n):\n>>> ').lower()
        if choice == 'y':
            stop = False
            reset(nice,mean,name)
        if choice == 'n':
            print (']nSorry to see you go')
            stop = False
            quit()
        else:
            print('\nEnter y for yes and n for no')



def reset(nice,mean,name):
    nice = 0
    mean = 0
    #notice i do not reset the name variable as the same user has elected to play again
    start1(nice,mean,name)
        
    








if __name__=='__main__':
    start1()
