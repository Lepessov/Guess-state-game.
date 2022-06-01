import pandas

from turtle import Turtle, Screen

states = pandas.read_csv('50_states.csv')
states_list = states.state.to_list()

states_guessed = list()
states_not_guessed = list()

screen = Screen()
screen.setup(width=730, height=500)
screen.bgpic('map.gif')

# Create turtle with coordinates and put on map
def create_state_info(states, state):
    state_info = states[states['state'] == state]
    state_x = int(state_info.x)
    state_y = int(state_info.y)
    state_locate = Turtle()
    state_locate.ht()
    state_locate.color('red')
    state_locate.penup()
    state_locate.goto(state_x, state_y)
    state_locate.write(f'{state}', 
                        align='center', 
                        font=('Arial', 10,  'normal'))


game = True
correct_answers = 0

while game:

    user_input = screen.textinput(title= f'{correct_answers}/50', 
            prompt='Enter the state name: ')

    # Type 'exit' to stop the app and see result
    if user_input.lower() == 'exit':
        for state in states_list:

            if state not in states_guessed:
                states_not_guessed.append(state)
                create_state_info(states, state)

        # Create dataframe with not guessed states and save them as 'csv' file
        df = pandas.DataFrame()
        df.to_csv('not_guessed_states.csv')
        game = False
        break

    # If user guesses state name state will appear on the map
    if user_input in states_list:
        correct_answers += 1
        create_state_info(states, user_input)
                 
            


screen.exitonclick()
