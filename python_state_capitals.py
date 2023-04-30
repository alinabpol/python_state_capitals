import random #import random module to generate a random number

#define a dictionary
us_state_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "St. Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

print('====== Welcome to the Learn US State Capitals! ========\n   Start the game by answering the questions below!\n============== To quit press "q" ======================')

def run_game():

    # create a tuple out of all keys from the dict to be able and pick random state through random.choice()
    states_tuple = tuple(us_state_capitals)
    # define a dict to count how many questions have been answered
    questions_counter = {True: 0, False: 0}
    asked_states = []
    score = 0

    print('What is the capital of this state?')
    while len(asked_states) < len(states_tuple):

        # declare a variable to hold a random state
        state = random.choice(states_tuple)
        while state in asked_states:
            state = random.choice(states_tuple)
        # add the state to the asked_states list
        asked_states.append(state)

        # provide a place for user's input
        answer = input(f"{state}: ")
        if answer in ('q'):
            break

        # declare a variable to verify user's reponse and return a boolean, by finding a capital in dict by the key(state), convert to lower case
        response = answer.lower() == us_state_capitals[state].lower()
        # increment questions_counter's appropriate key value by searching it with response boolean value (True or False)
        questions_counter[response] +=1
        if response:
            score +=1
            result = 'Correct!'
            print(f'Total of states answered correctly: {questions_counter[True]}')
        # a condition to check wether asked sates length equals to states_tuple (which is 50)
        elif len(asked_states) == len(states_tuple):
            play_again = input('Would you like to play again? (y/n): ')
            if play_again.lower() == 'y':
                run_game()
            else:
                print('Thanks for playing! Goodbye!')
                break
        else:
            result = f'Incorrect! The correct answer is {us_state_capitals[state]}'
        print(result)

    # create placeholders for args
    display_counts = 'Results: {}:{}, {}:{}'
    # declare a tuple to fill up display_counts placeholders
    args = ('Correct', questions_counter[True], 'Incorrect', questions_counter[False])
    print('-----------------------------------------------------')
    # unpack args tuple and replace placeholder with the values from args
    print(display_counts.format(*args))
    print(f"============== Your score is: {score} =====================")
    print('-----------------------------------------------------')
    

run_game()




