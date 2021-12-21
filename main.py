import random

stack = {"win": 0, "lose": 0, "draw": 0} #이긴횟수/진횟수/비긴횟수 저장

def win(stack): #이겼을시 함수
    print("Win!")
    stack["win"] += 1

def lose(stack): #졌을때 함수
    print("Lose!")
    stack["lose"] += 1

def draw(stack): #비겼을때 함수
    print("Draw!")
    stack["draw"] += 1

while True:
    program_choice = random.choice(['Rock', 'Scissors', 'Paper'])
    user_choice = input("Rock, Scissors, Paper? ")
    if user_choice == 'Rock' or user_choice == 'rock': #유저: 바위
        if program_choice == 'Rock': #프로그램: 바위
            draw(stack)
        elif program_choice =='Scissors': #프로그램: 가위
            win(stack)
        else: #프로그램: 보
            lose(stack)

    elif user_choice == 'Scissors' or user_choice == 'scissors': #유저: 가위
        if program_choice == 'Rock': #프로그램: 바위
            lose(stack)
        elif program_choice == 'Scissors': #프로그램: 가위
            draw(stack)
        else: #프로그램: 보
            win(stack)

    elif user_choice == 'Paper' or user_choice == 'paper': #유저: 보
        if program_choice == 'Rock':  #프로그램: 바위
            win(stack)
        elif program_choice =='Scissors': #프로그램: 가위
            lose(stack)
        else: #프로그램: 보
            draw(stack)

    else: #이상하게 입력했을때
        print('\nRock, Scissors, Paper 중 정확히 입력하여 주세요.')
        continue

    print("\nWin: {}/ Lose: {}/ Draw: {}".format(stack['win'], stack['lose'], stack['draw']))


    while True: #계속 할거임?
        to_be_continue = input('계속하시겠습니까?(y/n) :')
        if to_be_continue != 'y' and to_be_continue != 'n':
            print("\ny와 n 중 하나를 입력하여주세요.\n")
        elif to_be_continue == 'y':
            to_be_continue = True
            break
        else:
            to_be_continue = False
            break

    if not to_be_continue: #계속하기 싫을시 탈출
        break

print("\n\n게임이 종료되었습니다")