from random import choice
while True:
    userInput = str(input('Enter your choice [Rock/Paper/Scissor]:'))
    probableOutputs = ['rock', 'paper', 'scissor']
    systemOutput = choice(probableOutputs)
    print(f'System\'s choice: {systemOutput.title()}')
    if userInput.lower()==systemOutput:
        print('Game draw')
    elif userInput.lower()=='rock' and systemOutput == 'paper':
        print('You Lost')
    elif userInput.lower()=='rock' and systemOutput == 'scissor':
        print('You won !!')
    elif userInput.lower()=='paper' and systemOutput == 'rock':
        print('You won !!')
    elif userInput.lower()=='paper' and systemOutput == 'scissor':
        print('You lost !!')
    elif userInput.lower()=='scissor' and systemOutput == 'rock':
        print('You lost')
    elif userInput.lower()=='scissor' and systemOutput == 'paper':
        print('You won !!')
    else:
        print('Sorry, Couldn\'t recognize :(')