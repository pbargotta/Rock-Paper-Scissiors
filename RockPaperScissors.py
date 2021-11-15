import random

startRequest = input("Hello! Would you like to play 'Rock, Paper, Scissors'? ").lower()
if startRequest != "yes" and startRequest != "y":
    quit()

CPUOptions = ("rock", "paper", "scissors")

while True:
    scoreTo = int(input("What score would you like to play up to? "))
    CPUWins = 0
    playerWins = 0

    while playerWins < scoreTo and CPUWins < scoreTo:
        randomNum = random.randint(0, 2)
        CPUAnswer = CPUOptions[randomNum]
        print("CURRENT SCORE = PLAYER:", playerWins, "CPU:", CPUWins)
        playerAnswer = input("Would you like to go with 'Rock', 'Paper' or 'Scissors'? ").lower()
        while playerAnswer != "rock" and playerAnswer != "paper" and playerAnswer != "scissors":
            playerAnswer = input("Please pick 'Rock', 'Paper' or 'Scissors' this time. ").lower()
        if playerAnswer == "rock" and CPUAnswer == "scissors":
            print("CPU played 'scissors'. You won!")
            playerWins += 1
        if playerAnswer == "rock" and CPUAnswer == "paper":
            print("CPU played 'paper'. You lose.")
            CPUWins += 1
        if playerAnswer == "paper" and CPUAnswer == "rock":
            print("CPU played 'rock'. You won!")
            playerWins += 1
        if playerAnswer == "paper" and CPUAnswer == "scissors":
            print("CPU played 'scissors'. You lose.")
            CPUWins += 1
        if playerAnswer == "scissors" and CPUAnswer == "paper":
            print("CPU played 'paper'. You won!")
            playerWins += 1
        if playerAnswer == "scissors" and CPUAnswer == "rock":
            print("CPU played 'rock' You lose.")
            CPUWins += 1
        if playerAnswer == CPUAnswer:
            print("CPU played " + CPUAnswer + ". It's a draw!")

    print("GAME OVER")
    print("You lost the game.") if CPUWins == scoreTo else print("You won the game!")
    print("FINAL SCORE = PLAYER:", playerWins, " CPU:", CPUWins)
    playAgain = input("Would you like to play again? ").lower()

    if playAgain != "yes" and playAgain != "y":
        quit()