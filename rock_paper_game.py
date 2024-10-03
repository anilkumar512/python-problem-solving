your_score=0
computer_score=0
options={'rock','paper','scissor'}
while True:
    user_option=input('Enter your option(rock,paper,scissor,exit):')
    if user_option == exit or  your_score==10 or computer_score==10:
        break
    computer_option=options.pop()
    
    if user_option=='rock' and computer_option=='rock':
        print('Game is draw')
    elif user_option=='rock' and computer_option=='paper':
        print('Computer won')
        computer_score+=1
    elif user_option=='rock' and computer_option=='scissor':
        print('You won')
        your_score+=1
    elif user_option=='paper' and computer_option=='paper':
        print('Game is draw')
    elif user_option=='paper' and computer_option=='rock':
        print('You won')
        your_score+=1
    elif user_option=='paper' and computer_option=='scissor':
        print('Computer won')
        computer_score+=1
    elif user_option=='scissor' and computer_option=='scissor':
        print('Game is draw')
    elif user_option=='scissor' and computer_option=='rock':
        print('Computer won')
        computer_score+=1
    elif user_option=='scissor' and computer_option=='paper':
        print('You won')
        your_score+=1

    options.add(computer_option)
print(f'Your Score:{your_score}')
print(f'Computer Score:{computer_score}')